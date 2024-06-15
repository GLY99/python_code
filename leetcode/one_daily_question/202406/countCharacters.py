import collections

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars_mapping = collections.defaultdict(int)
        for char in chars:
            chars_mapping[char] += 1
        res = 0
        for word in words:
            match = True
            word_chars_mapping = collections.defaultdict(int)
            for char in word:
                word_chars_mapping[char] += 1
                if word_chars_mapping[char] > chars_mapping[char]:
                    match = False
                    break
            if match:
                res += len(word)
        return res