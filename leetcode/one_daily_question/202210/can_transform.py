class Solution:

    @staticmethod
    def can_transform(start: str, end: str) -> bool:
        """
        在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作
        一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"
        现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。
        :param start:
        :param end:
        :return:
        """
        length = len(start)
        i, j = 0, 0
        while i < length or j < length:
            while i < length and start[i] == 'X':
                i += 1
            while j < length and end[j] == 'X':
                j += 1
            # XXXL LXXX or RXXX XXXR
            if i == length or j == length:
                return i == j
            # 因为LR不能交换位置，所以start 和 end中遇到的第一个非X字符是一样的，
            if start[i] != end[j]:
                return False
            # 因为L只能向左移动，所以start中L的位置是大于等于end中L的位置
            if start[i] == "L" and i < j:
                return False
            # 因为R只能向右移动，所以start中R的位置是小于等于end中R的位置
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        # XXX XXL XXX XXX
        return i == j