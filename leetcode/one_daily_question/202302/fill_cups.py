from typing import List
import heapq


class Solution:
    @staticmethod
    def fill_cups(amount: List[int]) -> int:
        """
        fill cups
        :param amount:
        :return:
        """
        heap = []
        for num in amount:
            heapq.heappush(heap, -num)
        times = 0
        while True:
            max_num = -heapq.heappop(heap)
            mid_num = -heapq.heappop(heap)
            if mid_num == 0:
                times += max_num
                break
            heapq.heappush(heap, -(max_num - 1))
            heapq.heappush(heap, -(mid_num - 1))
            times += 1
        return times

    @staticmethod
    def fill_cups(amount: List[int]) -> int:
        """
        fill cups
        :param amount:
        :return:
        """
        sorted(amount)
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        else:
            return (sum(amount) + 1) // 2

