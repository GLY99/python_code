# https://leetcode.cn/problems/teemo-attacking/
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        expired = 0
        for time in timeSeries:
            if time >= expired:
                ans += duration
            else:
                ans += time + duration - expired
            expired = time + duration
        return ans