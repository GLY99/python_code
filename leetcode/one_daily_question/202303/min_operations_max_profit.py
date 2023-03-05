from typing import List


class Solution:
    def min_operations_max_profit(self, customers: List[int], boarding_cost: int, running_cost: int) -> int:
        """
        :param customers: 游玩人数
        :param boarding_cost: 游客花费
        :param running_cost: 运行成本
        :return: 最大利润
        """
        ans = 0
        wait = 0
        profile_sum = 0
        profile_max = 0
        for idx, customer in enumerate(customers):
            wait += customer
            boarding_customer = min(wait, 4)
            profile = boarding_customer * boarding_cost - running_cost
            profile_sum += profile
            if profile_sum > profile_max:
                profile_max = profile_sum
                ans = idx + 1
            wait -= boarding_customer
        idx += 1
        while wait > 0:
            idx += 1
            boarding_customer = min(wait, 4)
            profile = boarding_customer * boarding_cost - running_cost
            profile_sum += profile
            if profile_sum > profile_max:
                profile_max = profile_sum
                ans = idx
            wait -= boarding_customer
        return ans if profile_max > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    customers = [8, 3]
    boarding_cost = 5
    running_cost = 6
    print(sol.min_operations_max_profit(customers, boarding_cost, running_cost))