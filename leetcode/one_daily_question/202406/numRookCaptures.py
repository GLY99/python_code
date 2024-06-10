class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count, st, ed = 0, 0, 0
        for i, arr in enumerate(board):
            for j, v in enumerate(arr):
                if v == 'R':
                    st, ed = i, j
                    break
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            step = 0
            while True:
                tx = st + step * dx[i]
                ty = ed + step * dy[i]
                if tx < 0 or ty < 0 or tx >= 8 or ty >= 8 or board[tx][ty] == 'B':
                    break
                if board[tx][ty] == 'p':
                    count += 1
                    break
                step += 1
        return count