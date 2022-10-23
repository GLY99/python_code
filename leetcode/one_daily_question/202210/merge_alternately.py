class Solution:
    @staticmethod
    def merge_alternately(word1: str, word2: str) -> str:
        """
        给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串.
        如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
        返回 合并后的字符串
        :param word1:
        :param word2:
        :return:
        """
        word1_idx = 0
        word2_idx = 0
        length1 = len(word1)
        length2 = len(word2)
        ans = ""
        while word1_idx < length1:
            ans += word1[word1_idx]
            word1_idx += 1
            if word2_idx < length2:
                ans += word2[word2_idx]
                word2_idx += 1
            else:
                break
        if word1_idx < length1:
            ans += word1[word1_idx:]
        if word2_idx < length2:
            ans += word2[word2_idx:]
        return ans


if __name__ == "__main__":
    sol = Solution()
    w1 = "abcdefg"
    w2 = "pqr"
    print(sol.merge_alternately(w1, w2))