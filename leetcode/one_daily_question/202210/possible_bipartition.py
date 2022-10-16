from collections import deque
from typing import List


class Solution:
    @staticmethod
    def possible_bipartition(n: int, dislikes: List[List[int]]) -> bool:
        """
        给定一组n人（编号为1, 2, ..., n），我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
        给定整数 n和数组 dislikes，其中dislikes[i] = [ai, bi]，表示不允许将编号为 ai和bi的人归入同一组。
        当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
        :param n:
        :param dislikes:
        :return:
        """
        # 统计每个人不喜欢的人
        everyone_dislikes = [[] for _ in range(n)]
        for i, j in dislikes:
            everyone_dislikes[i - 1].append(j - 1)
            everyone_dislikes[j - 1].append(i - 1)
        # 染色数组，0表示下标为i的人没有被访问，1表示下标为i的人分在第1组，-1表示分在第二组
        color = [0] * n

        def dfs(idx: int, c: int) -> bool:
            # 下标为idx的人被分到了第c组，c 1 or -1
            color[idx] = c
            # 将下标为idx的人所有不喜欢的人放到第2组
            for dislike_idx in everyone_dislikes[idx]:
                # 不喜欢的人分到了同一组
                if color[dislike_idx] != 0 and color[dislike_idx] == color[idx]:
                    return False
                # 没有分过组，分到另外一组
                if color[dislike_idx] == 0 and not dfs(dislike_idx, -c):
                    return False
            return True

        for idx, c in enumerate(color):
            if c == 0 and not dfs(idx, 1):
                return False
        return True

    @staticmethod
    def possible_bipartition(n: int, dislikes: List[List[int]]) -> bool:
        """
        给定一组n人（编号为1, 2, ..., n），我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。
        给定整数 n和数组 dislikes，其中dislikes[i] = [ai, bi]，表示不允许将编号为 ai和bi的人归入同一组。
        当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。
        :param n:
        :param dislikes:
        :return:
        """
        # 统计每个人不喜欢的人
        everyone_dislikes = [[] for _ in range(n)]
        for i, j in dislikes:
            everyone_dislikes[i - 1].append(j - 1)
            everyone_dislikes[j - 1].append(i - 1)
        # 染色数组，0表示下标为i的人没有被访问，1表示下标为i的人分在第1组，-1表示分在第二组
        color = [0] * n
        for idx, c in enumerate(color):
            if c == 0:
                q = deque()
                q.append(idx)
                color[idx] = 1
                while q:
                    x = q.popleft()
                    for dislike_idx in everyone_dislikes[x]:
                        if color[dislike_idx] != 0 and color[dislike_idx] == color[x]:
                            return False
                        if color[dislike_idx] == 0:
                            color[dislike_idx] = -color[x]
                            q.append(dislike_idx)
        return True


if __name__ == "__main__":
    sol = Solution()
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(sol.possible_bipartition(n, dislikes))
