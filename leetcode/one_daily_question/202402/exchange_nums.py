from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = sum(numbers)
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers  

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2]
    print(sol.swapNumbers(nums))