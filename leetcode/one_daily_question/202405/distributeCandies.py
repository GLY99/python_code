# https://leetcode.cn/problems/distribute-candies/

class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        my_set = set()
        for t in candyType:
            my_set.add(t)
        ans = min(len(candyType) // 2, len(my_set))
        return ans
