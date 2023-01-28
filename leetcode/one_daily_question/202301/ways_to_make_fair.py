from typing import List


class Solution:
    @staticmethod
    def ways_to_make_fair(nums: List[int]) -> int:
        """
        ways_to_make_fair
        :param nums:
        :return:
        """
        ans = 0
        # 计算初始状态下的偶数和奇数下标和
        even_numbers, odd_numbers = 0, 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                even_numbers += num
            else:
                odd_numbers += num

        # 统计去掉数字之前的偶数下标和奇数下标和
        pre_even_numbers = 0
        pre_odd_numbers = 0

        # 遍历去掉每一个数字，检查是否满足平衡数组
        for idx, num in enumerate(nums):
            tmp_even_numbers = pre_even_numbers
            tmp_odd_numbers = pre_odd_numbers
            # 去掉的数字后面奇数下标和偶数下标会互换
            if idx % 2 == 0:
                next_even_numbers = even_numbers - pre_even_numbers - num
                next_odd_numbers = odd_numbers - pre_odd_numbers
                pre_even_numbers += num
            else:
                next_odd_numbers = odd_numbers - pre_odd_numbers - num
                next_even_numbers = even_numbers - pre_even_numbers
                pre_odd_numbers += num
            tmp_even_numbers += next_odd_numbers
            tmp_odd_numbers += next_even_numbers
            if tmp_even_numbers == tmp_odd_numbers:
                ans += 1
        return ans


if __name__ == '__main__':
    nums = [2, 1, 6, 4]
    print(Solution.ways_to_make_fair(nums))