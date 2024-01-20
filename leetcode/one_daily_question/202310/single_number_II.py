# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。

import collections
from typing import List


class Solution:
    def single_number(self, nums:List[int]) -> int:
        """
        single number
        """
        num_counter = collections.Counter(nums)
        ans = [num for num, count in num_counter.items() if count == 1][0]
        return ans
    
    def single_number(self, nums:List[int]) -> int:
        """
        single number
        """
        ans = 0
        for i in range(32):
            # 0 -> 31, 31是符号位
            total = sum((num >> i) & 1 for num in nums)
            if total % 3 != 0:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.single_number([-1]))
    # python中负数二进制位运算用补码（原码取反+1）计算
    print(bin(1))  # 00000000000000000000000000000001
    print(bin(-1))  # 10000000000000000000000000000001 => 11111111111111111111111111111111
    print(bin(-1 >> 1))
    print(bin(1 >> 1))
    print(1 << 31)  # 10000000000000000000000000000000
    ans = 0
    for i in range(31):
        ans += 2 ** i
    print(ans)
    print(ans - 2 ** 31)  # 01111111111111111111111111111111 - 10000000000000000000000000000000