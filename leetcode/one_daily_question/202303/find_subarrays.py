from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        """
        find sub arrays
        """
        length = len(nums)
        for i in range(0, length - 2):
            for j in range(i + 1, length - 1):
                if (nums[i] + nums[i + 1]) == (nums[j] + nums[j + 1]):
                    return True
        return False
    
    def findSubarrays(self, nums: List[int]) -> bool:
        """
        find sub arrays
        """
        sum_count = set()
        length = len(nums)
        for i in range(0, length - 1):
            sum = nums[i] + nums[i + 1]
            if sum in sum_count:
                return True
            sum_count.add(sum)
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.findSubarrays([4,2,4]))