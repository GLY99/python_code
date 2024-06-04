class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        length = len(s)
        res = [0] * length
        idx = -length
        for i, a in enumerate(s):
            if a == c:
                idx = i
            res[i] = i - idx
        idx = length * 2
        for i in range(length - 1, -1, -1):
            if s[i] == c:
                idx = i
            res[i] = min(res[i], idx - i)
        return res