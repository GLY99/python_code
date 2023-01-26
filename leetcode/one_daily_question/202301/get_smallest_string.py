from string import ascii_lowercase


class Solution(object):
    def get_smallest_string(self, n: int, k: int) -> str:
        """
        get smallest string
        :param n:
        :param k:
        :return: aaa..?zzz..
        """
        str_list = []
        a_count = 0
        for i in range(n):
            if (n - i - 1) * 26 >= (k - a_count):
                str_list.append(ascii_lowercase[0])
                a_count += 1
        else_count = (k - a_count) % 26
        if else_count != 0:
            str_list.append(ascii_lowercase[else_count - 1])
        z_count = (k - a_count) // 26
        str_list += z_count * ['z']
        return ''.join(str_list)

