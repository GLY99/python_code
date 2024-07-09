class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        length = len(columnTitle)
        ans = 0
        mult = 1
        for i in range(length - 1, -1, -1):
            k = ord(columnTitle[i]) - ord('A') + 1
            ans += k * mult
            mult *= 26
        return ans