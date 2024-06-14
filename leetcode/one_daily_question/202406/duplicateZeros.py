class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        count = 0
        i = 0
        while count < length:
            if arr[i] == 0:
                count += 2
            else:
                count += 1
            if count >= length:
                break
            i += 1
        j = length - 1
        if count == length + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            i -= 1