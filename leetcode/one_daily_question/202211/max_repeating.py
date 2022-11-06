class Solution:
    @staticmethod
    def max_repeating(sequence: str, word: str) -> int:
        """
        :param sequence:
        :param word:
        :return:
        """
        for i in range(int(len(sequence) / len(word)), -1, -1):
            if word * i in sequence:
                return i

    @staticmethod
    def max_repeating(sequence: str, word: str) -> int:
        """
        :param sequence:
        :param word:
        :return:
        """
        len_seq, len_word, ans = len(sequence), len(word), 0
        dp_arr = [0] * (len_seq + 10)
        for i in range(1, len_seq + 1):
            if i - len_word < 0:
                continue
            if sequence[i - len_word: i] == word:
                dp_arr[i] = dp_arr[i - len_word] + 1
            ans = max(ans, dp_arr[i])
        return ans


if __name__ == "__main__":
    s1 = "ababc"
    s2 = "ab"
    print(Solution.max_repeating(s1, s2))