from typing import List


class Solution:
    @staticmethod
    def advantage_count(nums1: List[int], nums2: List[int]) -> List[int]:
        """
        田忌赛马
        :param nums1:
        :param nums2:
        :return:
        """
        length = len(nums1)
        ans_list = [0] * length
        # nums1从小到大排序
        nums1 = sorted(nums1)
        # nums2从大到小排序
        copy_nums2 = enumerate(nums2)
        copy_nums2 = sorted(copy_nums2, key=lambda x: x[1], reverse=True)
        # 遍历copy_nums2
        left = 0
        right = length - 1
        for idx, val in copy_nums2:
            # 如果nums1中的最大值大于nums2中的最大值
            if nums1[right] > val:
                ans_list[idx] = nums1[right]
                right -= 1
            else:
                ans_list[idx] = nums1[left]
                left += 1
        return ans_list


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    sol = Solution()
    print(sol.advantage_count(nums1, nums2))