class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        idx = 0
        while candies > 0:
            res[idx % num_people] += min(idx + 1, candies)
            candies -= min(idx + 1, candies)
            idx += 1
        return res