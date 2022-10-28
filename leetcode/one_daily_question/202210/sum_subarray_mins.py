from typing import List


class Solution:
    @staticmethod
    def sum_subarray_mins(arr: List[int]) -> int:
        """
        给定一个整数数组 arr，找到 min(b)的总和，其中 b 的范围为 arr 的每个（连续）子数组。
        由于答案可能很大，因此 返回答案模 10^9 + 7 。
        :param arr:
        :return:
        """
        mod = 10 ** 9 + 7
        length, ans = len(arr), 0
        l_stack, r_stack = [-1] * length, [length] * length
        stack = []
        # 分别找到每个元素左右最近的小于它的元素位置
        for i in range(length):
            # 维护一个单调递增的栈
            while stack and arr[stack[-1]] >= arr[i]:
                r_stack[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in range(length - 1, -1, -1):
            # 维护一个单调递增的栈
            while stack and arr[stack[-1]] > arr[i]:
                l_stack[stack.pop()] = i
            stack.append(i)
        for i in range(length):
            a = i - l_stack[i]
            b = r_stack[i] - i
            ans += a * b * arr[i]
        return ans % mod


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 1, 2, 4]
    print(sol.sum_subarray_mins(arr))