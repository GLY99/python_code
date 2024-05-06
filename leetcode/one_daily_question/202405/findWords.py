class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        rowIdx = "12210111011122000010020202"
        for word in words:
            idx = rowIdx[ord(word[0].lower()) - ord('a')]
            add = True
            for c in word[1:]:
                if rowIdx[ord(c.lower()) - ord('a')] != idx:
                    add = False
                    break
            if add:
                ans.append(word)
        return ans