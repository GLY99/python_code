from typing import List


class Solution:
    @staticmethod
    def max_ascending_sum(nums: List[int]) -> int:
        """
        最大升序子数组和
        :param nums:
        :return:
        """
        max_sum = 0
        arr_sum = 0
        for idx, num in enumerate(nums):
            if idx == 0 or num > nums[idx - 1]:
                arr_sum += num
            else:
                arr_sum = num
            max_sum = max(max_sum, arr_sum)
        return max_sum

    @staticmethod
    def max_ascending_sum(nums: List[int]) -> int:
        """
        最大升序子数组和
        :param nums:
        :return:
        """
        dp_arr = list()
        for idx, num in enumerate(nums):
            dp_arr.append(num)
            if idx != 0 and num > nums[idx - 1]:
                dp_arr[idx] = num + dp_arr[idx - 1]
        return max(dp_arr)

    @staticmethod
    def max_ascending_sum(nums: List[int]) -> int:
        """
        最大升序子数组和
        :param nums:
        :return:
        """
        max_sum = 0
        length = len(nums)
        idx = 0
        while idx < length:
            s = nums[idx]
            idx += 1
            while idx < length and nums[idx] > nums[idx - 1]:
                s += nums[idx]
                idx += 1
            max_sum = max(s, max_sum)
        return max_sum
