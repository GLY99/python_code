class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        min + x = max - y
        ans = max - min - x - y
        ans = max - min - (x + y)
        0 <= x + y <= 2k
        ans最小的时候是x + y = 2k
        ans = max - min - 2k
        y = -2x + b
        """
        max_val = nums[0]
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i] < min_val:
                min_val = nums[i]
        ans = max_val - min_val - 2*k
        if ans > 0:
            return ans
        return 0