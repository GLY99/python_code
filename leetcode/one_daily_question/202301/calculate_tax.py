from typing import List


class Solution:
    def calculate_tax(self, brackets: List[List[int]], income: int) -> float:
        """
        calculate tax
        :param brackets:
        :param income:
        :return:
        """
        res = 0
        for idx, (upper, percent) in enumerate(brackets):
            if income <= 0:
                break
            percent = percent / 100.0
            sub_upper = brackets[idx][0] - (brackets[idx - 1][0] if idx != 0 else 0)
            tax = sub_upper
            if income >= sub_upper:
                res += sub_upper * percent
            else:
                res += income * percent
                tax = income
            income -= tax
        return res


if __name__ == '__main__':
    sol = Solution()
    brackets = [[3, 50], [7, 10], [12, 25]]
    income = 10
    print(sol.calculate_tax(brackets, income))
