class Solution:
    def count_asterisks(self, s: str) -> int:
        """
        count asterisks
        :param s:
        :return:
        """
        ans = 0
        count = 0
        for char in s:
            if char == '|':
                count += 1
                continue
            if count % 2 == 0 and char == '*':
                ans += 1
        return ans