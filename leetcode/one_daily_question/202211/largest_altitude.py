from typing import List


class Solution:
    @staticmethod
    def largest_altitude(gain: List[int]) -> int:
        """
        有一个自行车手打算进行一场公路骑行，这条路线总共由n + 1个不同海拔的点组成。自行车手从海拔为 0的点0开始骑行。
        给你一个长度为 n的整数数组gain，其中 gain[i]是点 i和点 i + 1的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。
        :param gain:
        :return:
        """
        count_h, max_h = 0, 0
        for g in gain:
            count_h += g
            max_h = max(count_h, max_h)
        return max_h
