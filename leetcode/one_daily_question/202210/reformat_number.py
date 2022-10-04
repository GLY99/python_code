class Solution:

    @staticmethod
    def reformat_number(number: str) -> str:
        """
        :param number:
        :return:
        """
        num_list = list()
        for char in number:
            if char.isdigit():
                num_list.append(char)
        length, idx = len(num_list), 0
        ans = list()
        while length > 0:
            # 如果当前剩余的数字个数大于4个，取三个
            if length > 4:
                ans.append("".join(num_list[idx: idx + 3]))
                idx += 3
                length -= 3
            # 如果剩余的数量小于等于4个，4个22分，小于4个直接为一组
            else:
                if length == 4:
                    ans.append("".join(num_list[idx: idx + 2]))
                    ans.append("".join(num_list[idx + 2: idx + 4]))
                else:
                    ans.append("".join(num_list[idx: idx + length]))
                break
        return '-'.join(ans)
