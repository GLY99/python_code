from typing import List


class Solution:
    @staticmethod
    def count_matches(items: List[List[str]], rule_key: str, rule_value: str) -> int:
        """
        :param items:
        :param rule_key:
        :param rule_value:
        :return:
        """
        count = 0
        idx = 0
        if rule_key == "color":
            idx = 1
        elif rule_key == "name":
            idx = 2
        for item in items:
            if item[idx] == rule_value:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    rule_key = "type"
    rule_value = "phone"
    print(sol.count_matches(items, rule_key, rule_value))