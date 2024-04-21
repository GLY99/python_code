import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []
        def dfs (target, idx, res, comb):
            if idx == len(candidates):
                return
            if target == 0:
                res.append(copy.deepcopy(comb))
                return
            dfs(target, idx + 1, res, comb)
            if target - candidates[idx] >= 0:
                comb.append(candidates[idx])
                dfs(target - candidates[idx], idx, res, comb)
                comb.pop()
        dfs(target, 0, res, comb)
        return res


if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = list_a[:2]
    list_a[0] = 0
    print(list_a, list_b) # [0, 2, 3] [1, 2]