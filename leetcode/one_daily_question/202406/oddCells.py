class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n
        for p in indices:
            rows[p[0]] += 1
            cols[p[1]] += 1
        ans = 0
        for row in rows:
            for col in cols:
                ans += (row + col) % 2
        return ans
