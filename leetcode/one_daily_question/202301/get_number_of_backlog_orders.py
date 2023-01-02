import heapq
from typing import List


class Solution:
    def get_number_of_backlog_orders(self, orders: List[List[int]]) -> int:
        """
        get_number_of_backlog_orders
        :param orders:
        :return:
        """
        mod = 10 ** 9 + 7
        buy_orders, sell_orders = [], []
        for price, amount, order_type in orders:
            if order_type == 0:
                # buy
                while amount > 0 and len(sell_orders) > 0 and sell_orders[0][0] <= price:
                    if sell_orders[0][1] > amount:
                        sell_orders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heapq.heappop(sell_orders)[1]
                if amount > 0:
                    heapq.heappush(buy_orders, [-price, amount])
            else:
                # sell
                while amount > 0 and len(buy_orders) > 0 and -buy_orders[0][0] >= price:
                    if buy_orders[0][1] > amount:
                        buy_orders[0][1] -= amount
                        amount = 0
                        break
                    amount -= heapq.heappop(buy_orders)[1]
                if amount > 0:
                    heapq.heappush(sell_orders, [price, amount])
        return (sum(amount for _, amount in buy_orders) + sum(amount for _, amount in sell_orders)) % mod
