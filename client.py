"""Bézier Curve & Parametric Surface Evaluation Engine
100% Python Standard Library.
"""

class BezierEvaluator:
    """de Casteljau's algorithm for polynomial curves and patches."""
    def de_casteljau_1d(self, points, t):
        pts = [list(p) for p in points]
        while len(pts) > 1:
            next_pts = []
            for i in range(len(pts) - 1):
                interp = [(1.0 - t) * pts[i][d] + t * pts[i + 1][d] for d in range(len(pts[0]))]
                next_pts.append(interp)
            pts = next_pts
        return [round(x, 4) for x in pts[0]]
