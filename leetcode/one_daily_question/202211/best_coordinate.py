from typing import List
import math


class Solution:
    def best_coordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        :param towers: towers[i] = [xi, yi, qi]
        :param radius:
        :return:
        """
        ans = [0, 0, 0]
        for i in range(51):
            for j in range(51):
                tmp_sum = 0
                for x, y, p in towers:
                    d = math.sqrt((x - i) * (x - i) + (y - j) * (y - j))
                    if d > radius:
                        continue
                    tmp_sum += int(p / (1 + d))
                if tmp_sum > ans[2]:
                    ans[2] = tmp_sum
                    ans[0] = i
                    ans[1] = j
        return [ans[0], ans[1]]

