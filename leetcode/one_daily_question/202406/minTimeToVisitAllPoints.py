class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        length = len(points)
        for idx, point in enumerate(points):
            if idx == length - 1:
                break
            x0, y0 = point[0], point[1]
            x1, y1 = points[idx + 1][0], points[idx + 1][1]
            ans += max(abs(x0 - x1), abs(y0 - y1))
        return ans