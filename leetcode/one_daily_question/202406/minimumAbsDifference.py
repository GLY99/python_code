class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        ans = []
        best_min = float('inf') # 正无穷大
        length = len(arr)
        for i in range(length - 1):
            delta = arr[i + 1] - arr[i]
            if delta < best_min:
                ans = [[arr[i], arr[i + 1]]]
                best_min = delta
            elif delta == best_min:
                ans.append([arr[i], arr[i + 1]])
        return ans