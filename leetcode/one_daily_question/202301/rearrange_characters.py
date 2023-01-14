from collections import Counter


class Solution:
    def rearrange_characters(self, s: str, target: str) -> int:
        """
        rearrange characters
        :param s:
        :param target:
        :return:
        """
        s_dict = Counter(s)
        target_dict = Counter(target)
        ans_dict = dict()
        for char, count in target_dict.items():
            ans = s_dict[char] // count
            ans_dict[char] = ans
        return min(ans_dict.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrange_characters(s="abbaccaddaeea", target="aaaaa"))
