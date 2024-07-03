class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        length = len(num)
        for i in range(length - 1, -1, -1):
            if num[i] != "0":
                break
        return num[0: i + 1]