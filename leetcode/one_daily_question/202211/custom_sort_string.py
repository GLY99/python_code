class Solution:
    @staticmethod
    def custom_sort_string(order: str, s: str) -> str:
        """
        给定两个字符串 order 和 s 。order 的所有单词都是 唯一 的，并且以前按照一些自定义的顺序排序。
        对 s 的字符进行置换，使其与排序的order相匹配。
        更具体地说，如果在order中的字符 x 出现字符 y 之前，那么在排列后的字符串中， x也应该出现在 y 之前。
        返回 满足这个性质的 s 的任意排列。没有出现在order中的字符可以在任意位置
        :param order:
        :param s:
        :return:
        """
        # 记录s中每个字符出现的次数
        char_mapping = dict()
        for c in s:
            char_mapping[c] = char_mapping.get(c, 0) + 1
        # 遍历order，如果order中的字符在s中出现，那么从字典中拿出全部排列
        ans_str = ''
        for c in order:
            if c in char_mapping:
                while char_mapping.get(c) > 0:
                    char_mapping[c] = char_mapping.get(c) - 1
                    ans_str = ans_str + c
        # 将s中没有出现在order中的字符全部排列在后面
        for c in char_mapping:
            while char_mapping.get(c) > 0:
                char_mapping[c] = char_mapping.get(c) - 1
                ans_str = ans_str + c
        return ans_str


if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    print(Solution.custom_sort_string(order, s))

