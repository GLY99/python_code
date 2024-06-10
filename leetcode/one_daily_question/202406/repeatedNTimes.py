import collections

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = collections.defaultdict(int)
        length = len(nums)
        for num in nums:
            mapping[num] += 1
        for k, v in mapping.items():
            if v == length / 2:
                return k
        return -1