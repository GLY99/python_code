class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        count = 0
        covers = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                count += v
                if v > 0:
                    covers += v - 1
                if i > 0:
                    covers += min(v, grid[i- 1][j])
                if j > 0:
                    covers += min(v, grid[i][j - 1])
        return count * 6 - covers * 2