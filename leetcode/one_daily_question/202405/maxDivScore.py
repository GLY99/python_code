class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        res = 0
        count = -1
        for divisor in divisors:
            tmp = 0
            for num in nums:
                if num % divisor == 0:
                    tmp += 1
            if tmp > count or (tmp == count and divisor < res):
                res = divisor
                count = tmp
        return res