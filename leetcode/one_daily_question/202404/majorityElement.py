class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        count = 0
        for v in nums:
            if count == 0:
                num = v
            if num == v:
                count += 1
            else:
                count -= 1
        return num