from typing import List


class Solution:
    def min_max_game(self, nums: List[int]) -> int:
        """
        min max game
        :param nums:
        :return:
        """
        length = len(nums)
        while length != 1:
            for i in range(0, int(length / 2)):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
            length /= 2
        return nums[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 2, 4, 8, 2, 2]
    print(sol.min_max_game(nums))