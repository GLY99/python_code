class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        for idx, num in enumerate(arr):
            j = idx + 1
            while j < len(arr):
                if arr[j] == 2 * num:
                    return True
                elif arr[j] > 2 * num:
                    break
                j += 1
        for idx in range(len(arr) - 1, -1, -1):
            j = idx - 1
            while j >= 0:
                if arr[j] == 2 * arr[idx]:
                    return True
                elif arr[j] < 2 * arr[idx]:
                    break
                j -= 1
        return False