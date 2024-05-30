import collections

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        collect_letters = collections.defaultdict(int)
        for letter in licensePlate:
            if letter.isalpha():
                collect_letters[letter.lower()] += 1
        res = ""
        for word in words:
            chars = collections.defaultdict(int)
            flag = True
            for char in word:
                chars[char.lower()] += 1
            for k, v in collect_letters.items():
                if chars[k] < v:
                    flag = False
                    break
            if not flag:
                continue
            if res == "" or len(word) < len(res):
                res = word
        return res