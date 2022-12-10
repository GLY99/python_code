class Solution:
    def check_powers_of_three(self, n: int) -> bool:
        """
        检查一个数时候可以组成三的幂相加
        """
        while n != 0:
            if n % 3 == 0 or n % 3 == 1:
                n = n // 3
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.check_powers_of_three(12))
