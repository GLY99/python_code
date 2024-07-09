class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        max_val_mapping = {}
        for i in range(len(matrix[0])):
            tmp_max = matrix[0][i]
            for j in range(len(matrix)):
                tmp_max = max(tmp_max, matrix[j][i])
            max_val_mapping[i] = tmp_max
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_val_mapping[j]
        return matrix