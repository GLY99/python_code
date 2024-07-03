class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        tmp_x = x
        while tmp_x > 0:
            tmp = tmp_x % 10
            tmp_x = tmp_x / 10
            res += tmp
        if x % res == 0:
            return res
        return -1