from typing import List


class Solution:
    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        """
        Given two string arrays word1 and word2, return true if the two arrays represent the same string,
        and false otherwise.
        A string is represented by an array if the array elements concatenated in order forms the string.
        :param word1:
        :param word2:
        :return:
        """
        return ''.join(word1) == ''.join(word2)

    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        """
        Given two string arrays word1 and word2, return true if the two arrays represent the same string,
        and false otherwise.
        A string is represented by an array if the array elements concatenated in order forms the string.
        :param word1:
        :param word2:
        :return:
        """
        w1, w2, i, j = 0, 0, 0, 0
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False
            i += 1
            j += 1
            if i == len(word1[w1]):
                w1 += 1
                i = 0
            if j == len(word2[w2]):
                w2 += 1
                j = 0
        return w1 == len(word1) and w2 == len(word2)