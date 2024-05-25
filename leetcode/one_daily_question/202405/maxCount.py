class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        mina = m
        minb = n
        for op in ops:
            mina = min(mina, op[0])
            minb = min(minb, op[1])
        return mina * minb