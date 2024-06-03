class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        for i, p in enumerate(points):
            for j, q in enumerate(points[:i]):
                for _, r in enumerate(points[:j]):
                    res = max(res, self.triangleArea(p[0], p[1], q[0], q[1], r[0], r[1]))
        return res
    
    def triangleArea(self, x1, y1, x2, y2, x3, y3):
        """
        triangleArea
        """
        return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2