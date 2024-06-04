class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy_area, xz_area, yz_area = 0, 0, 0
        for i, row in enumerate(grid):
            xz_max_height, yz_max_height = 0, 0
            for j, v in enumerate(row):
                if v > 0:
                    xy_area += 1
                xz_max_height = max(xz_max_height, v)
                yz_max_height = max(yz_max_height, grid[j][i])
            xz_area += xz_max_height
            yz_area += yz_max_height
        return xy_area + xz_area + yz_area