class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        length = len(arr)
        cur_max = arr[length - 1]
        arr[length - 1] = -1
        for i in range(length - 2, -1, -1):
            tmp = arr[i]
            arr[i] = cur_max
            cur_max = max(cur_max, tmp)
        return arr