from typing import List


class Solution:
    @staticmethod
    def build_array(target: List[int], n: int) -> List[str]:
        """
        给你一个数组 target 和一个整数 n。每次迭代，需要从list = { 1 , 2 , 3 ..., n } 中依次读取一个数字。
        请使用下述操作来构建目标数组 target ：
        "Push"：从 list 中读取一个新元素， 并将其推入数组中。
        "Pop"：删除数组中的最后一个元素。
        如果目标数组构建完成，就停止读取更多元素。
        题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。
        :param target:
        :param n:
        :return:
        """
        ans_list = []
        idx = 0
        for num in range(1, n + 1):
            if idx == len(target):
                break
            if num == target[idx]:
                ans_list.append("Push")
                idx += 1
            else:
                ans_list.append("Push")
                ans_list.append("Pop")
        return ans_list


if __name__ == "__main__":
    sol = Solution()
    target = [1, 3]
    n = 3
    print(sol.build_array(target, n))