class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        length = len(mountain)
        res = []
        for i in range(1, length - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
        return res