class Solution:
    @staticmethod
    def multiplication() -> None:
        """
        multiplication
        """
        for i in range(1, 10):
            for j in range(1, i + 1):
                print(f"{j}*{i}={i * j} ", end="")
            print('')


if __name__ == '__main__':
    print(Solution.multiplication())
