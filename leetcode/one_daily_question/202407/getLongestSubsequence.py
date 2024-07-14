class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        length = len(words)
        ans = []
        for i, x in enumerate(groups):
            if i == length - 1 or groups[i] != groups[i + 1]:
                ans.append(words[i])
        return ans