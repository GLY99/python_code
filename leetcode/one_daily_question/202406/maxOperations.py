class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        count = 0
        res = nums[0] + nums[1]
        for i in range(0, len(nums), 2):
            if i >= len(nums) - 1:
                break
            if nums[i] + nums[i + 1] == res:
                count += 1
            else:
                break
        return count