import sys
import json
from client import BezierEvaluator

bez = BezierEvaluator()

def handle_rpc(line):
    try:
        req = json.loads(line)
    except Exception:
        return
    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        res = {
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "genpark-bezier-curve-surface-evaluator-skill", "version": "1.0.0"},
            "capabilities": {"tools": {}}
        }
    elif method == "tools/list":
        res = {
            "tools": [
                {
                    "name": "evaluate_bezier",
                    "description": "Evaluate point on degree-N Bézier curve at parameter t in [0, 1]",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "control_points": {
                                "type": "array",
                                "items": {"type": "array", "items": {"type": "number"}}
                            },
                            "t": {"type": "number", "default": 0.5}
                        },
                        "required": ["control_points"]
                    }
                }
            ]
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_bezier":
            pts = args.get("control_points", [])
            t_val = args.get("t", 0.5)
            pt = bez.de_casteljau_1d(pts, t_val)
            res = {"content": [{"type": "text", "text": json.dumps({"point": pt, "t": t_val})}]}
        else:
            res = {"isError": True, "content": [{"type": "text", "text": f"Unknown tool {tool_name}"}]}
    else:
        res = {"error": {"code": -32601, "message": "Method not found"}}

    resp = {"jsonrpc": "2.0", "id": req_id, "result": res.get("result", res)}
    sys.stdout.write(json.dumps(resp) + "\n")
    sys.stdout.flush()

def main():
    for line in sys.stdin:
        if line.strip():
            handle_rpc(line.strip())

if __name__ == "__main__":
    main()
