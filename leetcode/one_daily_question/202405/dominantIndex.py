class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max_num = -1
        second_max_num = -1
        res = 0
        for idx, num in enumerate(nums):
            if num > first_max_num:
                second_max_num = first_max_num
                first_max_num = num
                res = idx
            elif num > second_max_num:
                second_max_num = num
        if first_max_num >= 2*second_max_num:
            return res
        return -1