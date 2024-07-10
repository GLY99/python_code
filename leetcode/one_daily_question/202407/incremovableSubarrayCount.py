class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum = 0
        for i in range(length):
            for j in range(i, length):
                if self.is_increase(nums, i, j):
                    sum += 1
        return sum


    def is_increase(self, nums, l, r):
        """
        is increase
        """
        for i in range(1, len(nums)):
            if i >= l and i <= r + 1:
                continue
            if nums[i] <= nums[i - 1]:
                return False
        if l - 1 >= 0 and r + 1 < len(nums) and nums[l - 1] >= nums[r + 1]:
            return False
        return True