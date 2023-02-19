import heapq
from typing import List


class Solution:
    def max_average_ratio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        max average ratio
        :param classes:
        :param extraStudents:
        :return:
        """
        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapq.heapify(h)
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(h)
            a, b = a + 1, b + 1
            heapq.heappush(h, (a / b - (a + 1) / (b + 1), a, b))
        return sum(v[1] / v[2] for v in h) / len(classes)
