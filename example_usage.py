from client import BezierEvaluator

def main():
    bez = BezierEvaluator()
    ctrl = [[0, 0], [1, 3], [3, 3], [4, 0]]
    mid = bez.de_casteljau_1d(ctrl, 0.5)
    print("Bézier Curve Evaluator Verification:")
    print(f"Control Points: {ctrl}")
    print(f"Mid-point at t=0.5: {mid}")

if __name__ == "__main__":
    main()
