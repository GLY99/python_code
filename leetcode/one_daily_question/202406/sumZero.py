class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(1, n/2+1):
            ans += [i, -i]
        if n % 2 != 0:
            ans.append(0)
        return ans