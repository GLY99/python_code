from typing import List, Tuple
from functools import cache


class Solution:
    def max_happy_groups(self, batch_size: int, groups: List[int]) -> int:
        """
        max happy groups
        :param batchSize:
        :param groups:
        :return:
        """
        cnt = [0] * batch_size
        for group in groups:
            cnt[group % batch_size] += 1

        @cache
        def dfs(left: int, cnt: Tuple[int]) -> int:
            """
            dfs
            :param left:
            :param cnt:
            :return:
            """
            res = 0
            cnt = list(cnt)
            for i, c in enumerate(cnt):
                if c > 0:
                    cnt[i] -= 1
                    # i == 0 表示剩余 i + 1 面包， left是上次剩下的面包
                    # left为0表示上次没有剩余面包，所以这次一定会有一个人开心
                    res = max(res, (left == 0) + dfs((left + i + 1) % batch_size, tuple(cnt)))
                    cnt[i] += 1
            return res

        return cnt[0] + dfs(0, tuple(cnt[1:]))


if __name__ == '__main__':
    sol = Solution()
    batchsize = 4
    groups = [1, 3, 2, 5, 2, 2, 1, 6]
    print(sol.max_happy_groups(batchsize, groups))