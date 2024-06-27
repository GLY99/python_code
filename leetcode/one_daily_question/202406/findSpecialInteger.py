class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        length = len(arr)
        while end < length:
            while end < length and arr[end] == arr[start]:
                end += 1
            if (end - start) * 4 > length:
                return arr[start]
            start = end
        return -1