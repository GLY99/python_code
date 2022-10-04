class Solution:

    @staticmethod
    def check_ones_segment(s: str) -> bool:
        """
        判断字符串时候由左边连续的1和右边连续的0组成
        :param s:
        :return: bool
        """
        start_idx = 0
        end_idx = len(s) - 1
        while start_idx < len(s):
            if s[start_idx] == '1':
                start_idx += 1
            else:
                break
        while end_idx > 0:
            if s[end_idx] == '0':
                end_idx -= 1
            else:
                break
        return (start_idx - end_idx) == 1

    @staticmethod
    def check_ones_segment(s: str) -> bool:
        """
        判断字符串时候由左边连续的1和右边连续的0组成
        :param s:
        :return: bool
        """
        return "01" not in s
