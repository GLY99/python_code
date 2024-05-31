class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        length = len(grid)
        arr = [0] * length*length
        for i in range(length):
            for j in range(length):
                arr[grid[i][j] - 1] += 1
        return [arr.index(2) + 1, arr.index(0) + 1]