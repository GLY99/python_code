class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        minfreq = [float("inf")] * 26
        for word in words:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            for i in range(26):
                minfreq[i] = min(freq[i], minfreq[i])
        ans = []
        for i, count in enumerate(minfreq):
            while count > 0:
                ans.append(chr(i + ord('a')))
                count -= 1
        return ans