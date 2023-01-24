from typing import List


class Solution:
    def count_points(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        count points
        :param points:
        :param queries:
        :return:
        """
        ans = []
        for x1, y1, r in queries:
            count = 0
            for x2, y2 in points:
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r ** 2:
                    count += 1
            ans.append(count)
        return ans
