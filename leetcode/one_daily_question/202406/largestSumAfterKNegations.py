class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = 0
        for idx, num in enumerate(nums):
            if num <= 0 and k > 0:
                nums[idx] = -num
                k -= 1
            ans += nums[idx]
        nums = sorted(nums)
        if k % 2 == 0:
            return ans
        else:
            return ans - 2 * num[0]