class Solution:
    def num_tilings(self, n: int) -> int:
        """
        有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
        给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10^9 + 7 取模 的值。
        f1 = 1
        f2 = 2
        f3 = f2 + f1 +2
        f4 = f3 + f2 + f1 * 2 +2 = f3 + f2 + 2(f1 + 1)
        f5 = f4 + f3 + 2(f2 + f1 +2)
        f[n - 1] = f(n - 2) + f(n - 3) + ... + 2(f[n - 4] + f[n - 5] + ... + f1 + 1)
        fn = f(n - 1) + f(n - 2) + ... + 2(f[n - 3] + f[n - 4] + ... + f1 + 1)
        fn - f[n - 1] = f[n - 1] + f[n-3]
        fn = 2f[n - 1] + f[n- 3]
        :param n:
        :return:
        """
        if n == 1:
            return 1
        mod = 10 ** 9 + 7
        dp_arr = [0] * (n + 1)
        dp_arr[0] = 1
        dp_arr[1] = 1
        dp_arr[2] = 2
        for n in range(3, n + 1):
            dp_arr[n] = (2 * dp_arr[n - 1] + dp_arr[n - 3]) % mod
        return dp_arr[n]

    def num_tilings(self, n: int) -> int:
        """
        有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
        给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10^9 + 7 取模 的值。
        :param n:
        :return:
        """
        if n == 1:
            return 1
        mod = 10 ** 9 + 7
        a = 1 # n - 3
        b = 1
        c = 2 # n - 1
        for n in range(3, n + 1):
            a, b, c = b, c, (2 * c + a) % mod
        return c
