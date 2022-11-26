from typing import List


class Solution(object):

    def expressive_words(self, s: str, words: List[str]) -> int:
        """
        expressive words
        对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张
        扩张操作定义如下：选择一个字母组（包含字母c），然后往其中添加相同的字母c使其长度达到 3 或以上
        解法：
        首先如果对某个字母进行扩张，那必须扩张到3或以上。我们以s中的字母作为标准，来检验word中字母是否满足条件
        1.当s中的连续重复字母数量小于3个，那么不能对word中对应的字母扩张，不满足扩张条件,此时需要s和word中重复字母数量相等
        2.当s中连续的字母数量大于等于3个时，可以对word中的字母扩张到和s数量相等，此时需要word中重复数量小于s
        """
        result = 0
        for word in words:
            result += 1 if self.stretchy_word(s, word) else 0
        return result

    @staticmethod
    def stretchy_word(s: str, word: str) -> bool:
        """
        stretchy word
        """
        s_length = len(s)
        word_length = len(word)
        if word_length > s_length:
            return False
        p1, p2 = 0, 0
        while p1 < s_length and p2 < word_length:
            flag_word = s[p1]
            c1, c2 = 0, 0
            while p1 < s_length and s[p1] == flag_word:
                p1 += 1
                c1 += 1
            while p2 < word_length and word[p2] == flag_word:
                p2 += 1
                c2 += 1
            if (c1 < 3 and c1 != c2) or c1 < c2:
                return False
        return p1 == s_length and p2 == word_length


if __name__ == "__main__":
    sol = Solution()
    words = ["hello"]
    s = "heeellooo"
    print(sol.expressive_words(s, words))
