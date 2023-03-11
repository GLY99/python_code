from typing import List


class Solution:
    def findLongest_subarray(self, array: List[str]) -> List[str]:
        """
        findLongest_subarray
        :param array: 包含字母数字的array
        :return: 字母数字个数一样的最长子区间
        """
        char_count = 0
        num_count = 0
        max_length = 0
        start_idx = 0
        idx = {0: -1}
        for i, s in enumerate(array):
            if s.isdigit():
                num_count += 1
            else:
                char_count += 1
            a = char_count - num_count
            if a in idx:
                if i - idx[a] > max_length:
                    max_length = i - idx[a]
                    start_idx = idx[a] + 1
            else:
                idx[a] = i
        return array[start_idx: start_idx + max_length]
