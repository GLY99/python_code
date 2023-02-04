from typing import List


class Solution:
    def get_maximum_consecutive(self, coins: List[int]) -> int:
        """
        get maximum consecutive
        :param coins:
        :return:
        """
        coins = sorted(coins)
        res = 1
        for coin in coins:
            if coin > res:
                break
            else:
                res += coin
        return res

