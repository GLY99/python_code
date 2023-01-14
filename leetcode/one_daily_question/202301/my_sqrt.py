class Solution:
    def my_sqrt(self, x: int) -> int:
        """
        my sqrt
        :param x:
        :return:
        """
        if x < 1:
            return x
        left, right, ans = 0, x, 0
        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.my_sqrt(9))
