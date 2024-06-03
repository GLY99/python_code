class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        lines, count = 1, 0
        for c in s:
            count += widths[ord(c) - ord('a')]
            if count > 100:
                count = widths[ord(c) - ord('a')]
                lines += 1
        return lines, count