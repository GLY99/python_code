class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sorted_heights = sorted(heights)
        res = 0
        for idx, v in enumerate(heights):
            if v != sorted_heights[idx]:
                res += 1
        return res