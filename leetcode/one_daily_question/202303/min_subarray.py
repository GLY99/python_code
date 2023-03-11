from typing import List


class Solution:
    def min_subarray(self, nums: List[int], p: int) -> int:
        """
        min_subarray
        :param nums: 数字数组
        :param p: 数字p
        :return: 移除最短的子数组，让剩余数字可以被p整除
        """
        # 找前缀和是x、target的最短数组
        x = 0
        for num in nums:
            x = (x + num) % p
        if x == 0:
            return 0
        min_length = len(nums)
        pre_count = 0
        idx = {0: -1}
        for i, num in enumerate(nums):
            pre_count = (pre_count + num) % p
            target = (pre_count - x + p) % p
            if target in idx:
                min_length = min(min_length, i - idx[target])
            idx[pre_count] = i
        return -1 if min_length == len(nums) else min_length
