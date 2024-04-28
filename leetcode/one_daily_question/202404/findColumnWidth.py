class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid[0])
        res = [0] * n
        for i, arr in enumerate(grid):
            for j, num in enumerate(arr):
                length = 0
                if num <= 0:
                    length = 1
                    num = -num
                while num != 0:
                    num = num // 10 # 向左取整， 1.2 -> 1, -1.2 -> -2
                    length += 1
                res[j] = max(res[j], length)
        return res


if __name__ == '__main__':
    grid = [[-12]]
    Solution().findColumnWidth(grid)
