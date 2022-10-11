class Solution:
    @staticmethod
    def are_almost_equal(s1: str, s2: str) -> bool:
        """
        给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），
        并交换这两个下标所对应的字符。
        如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。
        :param s1:
        :param s2:
        :return:
        """
        idx_list = []
        for idx, char in enumerate(s1):
            if len(idx_list) > 2:
                return False
            if char != s2[idx]:
                idx_list.append(idx)
        if len(idx_list) == 0:
            return True
        elif len(idx_list) != 2:
            return False
        return s1[idx_list[0]] == s2[idx_list[1]] and s1[idx_list[1]] == s2[idx_list[0]]


if __name__ == "__main__":
    s1 = "attack"
    s2 = "defend"
    sol = Solution()
    print(sol.are_almost_equal(s1, s2))