class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums_sum = sum(nums)
        prefix_sum = 0
        for i in range(length):
            if nums_sum - nums[i] - 2*prefix_sum == 0:
                return i
            prefix_sum += nums[i]
        return -1


if __name__ == "__main__":
    s = Solution()
    s.pivotIndex([2, 1, -1])