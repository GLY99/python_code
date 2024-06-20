class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        length = len(nums)
        for i in range(length):
            while nums[i] >= 10:
                nums[i] = nums[i] // 10
            for j in range(i + 1, length):
                if self.gcd(nums[i], nums[j] % 10) == 1:
                    res += 1
        return res
    
    def gcd(self, x, y):
        """
        gcd
        """
        while y != 0:
            tmp = x % y
            x = y
            y = tmp
        return x
