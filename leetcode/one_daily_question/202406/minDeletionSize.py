class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if j <= len(strs) - 2 and strs[j][i] > strs[j + 1][i]:
                    ans += 1
                    break
        return ans