from typing import List


class Solution:
    @staticmethod
    def min_swap(nums1: List[int], nums2: List[int]) -> int:
        """
        有两个长度相等且不为空的整型数组 nums1 和 nums2;在一次操作中，交换 nums1[i] 和 nums2[i]的元素
        返回 使 nums1 和 nums2 严格递增 所需操作的最小次数
        严格递增： arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1]
        :param nums1:
        :param nums2:
        :return:
        """
        length = len(nums1)
        # dp_num [[i, j], [i, j] ...] 每个位置不发生交换的最小交换次数i,和发生交换的次数j
        dp_num = [[0, 0] for _ in range(length)]
        for i in range(1, length):
            dp_num[i][0] = dp_num[i][1] = length
        # 位置0要么交换要么不交换
        dp_num[0][1] = 1
        for i in range(1, length):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                # 如果i i-1 位置nums1 nums2顺序满足递增，i 和 i-1位置要么都交换要么都不交换
                dp_num[i][0] = dp_num[i - 1][0]
                dp_num[i][1] = dp_num[i - 1][1] + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                # 如果i i-1 位置nums1 nums2交叉满足递增， i 和 i-1位置只能有一个位置进行交换
                dp_num[i][0] = min(dp_num[i - 1][1], dp_num[i][0])
                dp_num[i][1] = min(dp_num[i - 1][0] + 1, dp_num[i][1])
        return min(dp_num[length - 1][0], dp_num[length - 1][1])

    @staticmethod
    def min_swap(nums1: List[int], nums2: List[int]) -> int:
        """
        有两个长度相等且不为空的整型数组 nums1 和 nums2;在一次操作中，交换 nums1[i] 和 nums2[i]的元素
        返回 使 nums1 和 nums2 严格递增 所需操作的最小次数
        严格递增： arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1]
        :param nums1:
        :param nums2:
        :return:
        """
        length = len(nums1)
        unchanged_min_count = 0
        change_min_count = 1
        for i in range(1, length):
            cur_unchanged_count = cur_change_count = length
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                cur_unchanged_count = unchanged_min_count
                cur_change_count = change_min_count + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                cur_unchanged_count = min(cur_unchanged_count, change_min_count)
                cur_change_count = min(cur_change_count, unchanged_min_count + 1)
            unchanged_min_count = cur_unchanged_count
            change_min_count = cur_change_count
        return min(change_min_count, unchanged_min_count)


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3, 5, 4]
    nums2 = [1, 2, 3, 7]
    print(sol.min_swap(nums1, nums2))

