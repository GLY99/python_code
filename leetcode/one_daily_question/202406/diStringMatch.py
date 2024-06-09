class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        length = len(s)
        ans = [0] * (length + 1)
        left = 0
        right = length
        for idx, v in enumerate(s):
            if v == 'I':
                ans[idx] = left
                left += 1
            elif v == 'D':
                ans[idx] = right
                right -= 1

        ans[length] = left
        return ans