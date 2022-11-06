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

    def beat_coordinate(self, towers: List[List[int]], redius: int) -> List[int]:
        g = [[0] * 101 for _ in range(101)]
        ans = [0, 0, 0]
        for x, y , p in towers:
            for i in range(0, x + redius + 1):
                for j in range(0, y + redius + 1):
                    d = math.sqrt((x - i) * (x - i) + (y - j) * (y - j))
                    if d > redius:
                        continue
                    g[i][j] += int(p / (1 + d))
                    if g[i][j] > ans[2]:
                        ans[2] = g[i][j]
                        ans[0] = i
                        ans[1] = j
                    elif g[i][j] == ans[2] and (i < ans[0] or (i == ans[0] and j < ans[1])):
                        ans[0] = i
                        ans[1] = j
        return [ans[0], ans[1]]

