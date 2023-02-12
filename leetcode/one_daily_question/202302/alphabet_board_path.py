class Solution:
    def alphabet_board_path(self, target: str) -> str:
        """
        alphabet board path
        :param target:
        :return:
        """
        i, j = 0, 0
        ans = ""
        for c in target:
            row, col = int(ord(c) - ord('a')) // 5, int(ord(c) - ord('a')) % 5
            while i > col:
                i -= 1
                ans += 'L'
            while j > row:
                j -= 1
                ans += 'U'
            while i < col:
                i += 1
                ans += 'R'
            while j < row:
                j += 1
                ans += 'D'
            ans += '!'
        return ans


if __name__ == '__main__':
    sol = Solution()
    target = "leet"
    print(sol.alphabet_board_path(target))