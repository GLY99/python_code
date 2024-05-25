import collections

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        mapping = collections.defaultdict(int)
        for _, num in enumerate(nums):
            mapping[num] += 1
            if mapping[num] > 1:
                res[0] = num
        for i in range(1, len(nums) + 1):
            if mapping.get(i, -1) == -1:
                res[1] = i
        return res

    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums = sorted(nums)
        res = [0, 0]
        if nums[0] != 1:
            res[1] = 1
        elif nums[length - 1] != length:
            res[1] = length
        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                res[0] = nums[i]
            if nums[i + 1] - nums[i] > 1:
                res[1] = nums[i] + 1
        return res