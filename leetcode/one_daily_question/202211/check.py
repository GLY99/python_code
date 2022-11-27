from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。
        如果nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。
        """
        count = 0
        length = len(nums)
        for idx, num in enumerate(nums):
            if num > nums[(idx + 1) % length]:
                count += 1
            if count > 1:
                return False
        return True
