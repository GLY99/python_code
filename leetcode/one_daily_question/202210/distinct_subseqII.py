class Solution:
    @staticmethod
    def distinct_subseq(s: str) -> int:
        """
        给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
        字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
        s = "abc" -> 7 "a", "b", "c", "ab", "ac", "bc", "abc"。
        :param s:
        :return:
        """
        length, mod = len(s), 1e9+7
        # 长度为 0-length的字符串，每个位置以字符串a-z结尾的数量
        # [0] * 26中只有一个位置不为0，因为每个位置字母的确定的
        dp = [[0] * 26 for _ in range(length + 1)]
        for i in range(1, length + 1):
            # 计算下标 0-25 a-z
            char_num = ord(s[i - 1]) - ord('a')
            for j in range(0, 26):
                # 如果计算第i个位置以j结尾的子序列个数，分两个情况：
                # 1.第i个位置不是j，那么子序列个数为dp[i - 1][j]
                # 2.第i个位置是j，那么子序列个数为1 + dp[i - 1][0] + ... + dp[i - 1][25]
                dp[i][j] = dp[i - 1][j] if char_num != j else (1 + sum(dp[i - 1])) % mod
        return int(sum(dp[length]) % mod)

    @staticmethod
    def distinct_subseq(s: str) -> int:
        """
        给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。
        字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
        s = "abc" -> 7 "a", "b", "c", "ab", "ac", "bc", "abc"。
        :param s:
        :return:
        """
        length, mod, ans = len(s), 1e9 + 7, 0
        # 长度为 0-length的字符串，每个位置以字符串a-z结尾的数量
        dp = [0] * 26
        for i in range(length):
            # 计算下标 0-25 a-z
            char_num = ord(s[i - 1]) - ord('a')
            pre_count = dp[char_num]
            dp[char_num] = (ans + 1) % mod  # 单独作为一个子序列+前面位置的子序列数
            ans = (ans + dp[char_num] - pre_count) % mod
        return int(ans)


if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    print(sol.distinct_subseq(s))