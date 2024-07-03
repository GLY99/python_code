class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        length = len(nums)
        for i in range(0, length - 1, 2):
            for j in range(nums[i]):
                ans.append(nums[i + 1])
        return ans