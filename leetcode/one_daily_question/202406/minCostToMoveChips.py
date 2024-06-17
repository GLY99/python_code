class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        ans = [0, 0]
        for _, p in enumerate(position):
            ans[p % 2] += 1
        return min(ans[0], ans[1])