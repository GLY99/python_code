class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for idx, num in enumerate(nums):
            if num != idx:
                return idx
        return len(nums)