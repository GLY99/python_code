import collections

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        start = 0
        ans = 0
        for end, num in enumerate(nums):
            while num - nums[start] > 1:
                start += 1
            if num - nums[start] == 1 and end - start + 1 > ans:
                ans = end - start + 1
        return ans
    
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_map = collections.defaultdict(int)
        for num in nums:
            my_map[num] += 1
        
        ans = 0
        for num in nums:
            if my_map[num + 1] > 0 and my_map[num] + my_map[num + 1] > ans:
                ans = my_map[num] + my_map[num + 1]
        return ans
        