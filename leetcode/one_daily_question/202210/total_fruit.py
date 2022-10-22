from typing import List


class Solution:
    @staticmethod
    def total_fruit(fruits: List[int]) -> int:
        """
        :param fruits:
        :return:
        """
        bucket = dict()
        left = 0
        ans = 0
        for right, fruit in enumerate(fruits):
            bucket[fruit] = bucket.get(fruit, 0) + 1
            while len(bucket) > 2:
                bucket[fruits[left]] -= 1
                if bucket[fruits[left]] == 0:
                    bucket.pop(fruits[left])
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    fruits = [1, 2, 1]
    print(sol.total_fruit(fruits))