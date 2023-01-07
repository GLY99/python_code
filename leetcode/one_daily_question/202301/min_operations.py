from typing import List


class Solution:
    def min_operations(self, nums: List[int], x: int) -> int:
        """
        min operations
        两端和为x,那么剩余的和就为sum(nums) - x, sum(nums) - x 片段越多，操作次数越小
        :param nums:
        :param x:
        :return:
        """
        sum_count = sum(nums)
        length = len(nums)
        target = sum_count - x
        left_idx = 0
        sub_count = 0
        res = -1
        for right_idx in range(length):
            sub_count += nums[right_idx]
            while left_idx <= right_idx and sub_count > target:
                sub_count -= nums[left_idx]
                left_idx += 1
            if sub_count == target:
                res = max(res, right_idx - left_idx + 1)
        return length - res if res >= 0 else -1

