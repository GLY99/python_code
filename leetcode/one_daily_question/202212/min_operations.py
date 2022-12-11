from typing import List


class Solution:
    def min_operations(self, nums: List[int]) -> int:
        """
        最少次数使数组递增
        :param nums:
        :return:
        """
        ans, max_num = 0, 0
        for num in nums:
            if num <= max_num:
                ans += max_num + 1 - num
            max_num = max(max_num + 1, num)
        return ans
