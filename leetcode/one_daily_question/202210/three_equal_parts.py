from typing import List


class Solution:
    @staticmethod
    def three_equal_parts(arr: List[int]) -> List[int]:
        """
        把一个列表分成二进制大小相等的三部分
        arr = [(1),0,1,(0),1]
        输出：[0,3]
        :param arr:
        :return: [first_end_idx, third_start_idx]
        """
        arr_length = len(arr)
        arr_sum = sum(arr)
        # 如果arr可以被分成二进制大小相等的三部分，每部分1的数量一样
        if arr_sum % 3 != 0:
            return [-1, -1]
        if arr_sum == 0:
            return [0, arr_length - 1]
        # 每部分1的数量
        one_count = arr_sum / 3
        first = second = third = cur = 0
        # 找到每部分最左边1的位置
        for idx, val in enumerate(arr):
            if val:
                # 每部分1开始的位置
                if cur == 0:
                    first = idx
                elif cur == one_count:
                    second = idx
                elif cur == one_count * 2:
                    third = idx
                cur += 1
        # 第三部分的1和后置0是固定的，大小也是固定的，以第三部分作为标准划分没有前导0的长度
        available_length = arr_length - third
        # 比较三部分每个位置数字是否一样
        if first + available_length <= second and second + available_length <= third:
            i = 0
            while third + i < arr_length:
                if (arr[first + i] != arr[second + i]) or (arr[first + i] != arr[third + i]):
                    return [-1, -1]
                i += 1
            return [first + available_length - 1, second + available_length]
        return [-1, -1]


if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1]
    sol = Solution()
    print(sol.three_equal_parts(arr))
