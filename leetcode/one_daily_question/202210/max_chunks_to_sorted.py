from typing import List


class Solution(object):
    @staticmethod
    def max_chunks_to_sorted(arr: List[int]) -> int:
        """
        给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。
        我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。
        返回数组能分成的最多块数量。
        [4,3,2,1,0] > 1
        [1,0,2,3,4] > 4
        :param arr:
        :return:
        """
        length = len(arr)
        count = 0
        left = 0
        range_max_num = -1
        range_min_num = length
        for right in range(length):
            range_max_num, range_min_num = max(range_max_num, arr[right]), min(range_min_num, arr[right])
            # 如果一个区间的最大值等于这个区间右边界的下标，最小值等于左边界下标
            # 说明这个区间就是 left -> right 所有数字的集合，排序后一定是升序
            if left == range_min_num and right == range_max_num:
                count += 1
                left = right + 1
                range_max_num = -1
                range_min_num = length
        return count


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 0, 2, 3, 4]
    print(sol.max_chunks_to_sorted(arr))
