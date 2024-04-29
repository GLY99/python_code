# https://leetcode.cn/problems/sort-the-matrix-diagonally/?envType=daily-question&envId=2024-04-29

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        diag = [[] for i in range(m + n)]
        # 将对角线元素放入各自的矩阵
        for i, arr in enumerate(mat):
            for j, num in enumerate(arr):
                diag[i - j + n].append(num)
        
        # 对对角线元素进行排序
        for arr in diag:
            arr.sort()
        
        # 重新放回mat
        for i, _ in enumerate(mat):
            for j, _ in enumerate(mat[i]):
                mat[i][j] = diag[i - j + n].pop(0)
        return mat