class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_cnt = 0
        self.arr = [[] for i in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.arr[index].append((self.snap_cnt, val))

    def snap(self):
        """
        :rtype: int
        """
        ans = self.snap_cnt
        self.snap_cnt += 1
        return ans


    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        length = len(self.arr[index])
        left, right = 0, length
        while left < right:
            mid = (left + right) >> 1
            if self.arr[index][mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid
        if left <= 0:
            return 0
        return self.arr[index][left - 1][1]