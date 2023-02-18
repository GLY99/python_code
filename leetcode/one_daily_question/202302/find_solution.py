from typing import List


class Solution:
    def find_solution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        find solution
        :param customfunction:
        :param z:
        :return:
        """
        res = []
        for i in range(1, 1000):
            for j in range(1, 1000):
                if customfunction.f(i, j) == z:
                    res.append([i, j])
                    break
                if customfunction.f(i, j) > z:
                    break

        return res

    def find_solution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        find solution
        :param customfunction:
        :param z:
        :return:
        """
        ans = []
        y = 1000
        for x in range(1, 1001):
            while y and customfunction.f(x, y) > z:
                y -= 1
            if y == 0:
                break
            if customfunction.f(x, y) == z:
                ans.append([x, y])
        return ans

    def find_solution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        find solution
        :param customfunction:
        :param z:
        :return:
        """
        ans = []
        for x in range(1, 1001):
            left, right = 1, 1000
            while left <= right:
                mid = (left + right) // 2
                if customfunction.f(x, mid) == z:
                    ans.append([x, mid])
                    break
                elif customfunction.f(x, mid) < z:
                    left = mid + 1
                else:
                    right = mid - 1
        return ans


