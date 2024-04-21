import copy

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        def dfs(cur, target, res, tmp):
            if target == 0 and len(tmp) == k:
                res.append(copy.deepcopy(tmp))
                return
            if len(tmp) > k or cur > target or cur > 9:
                return
            tmp.append(cur)
            dfs(cur + 1, target - cur, res, tmp)
            tmp.pop()
            dfs(cur + 1, target, res, tmp)
        dfs(1, n, res, tmp)
        return res