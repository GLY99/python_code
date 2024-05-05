# https://leetcode.cn/problems/defuse-the-bomb/?envType=daily-question&envId=2024-05-05
import copy


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp_code = copy.deepcopy(code)
        code_length = len(code)
        for idx, _ in enumerate(temp_code):
            new_code = 0
            if k > 0:
                i = (idx + 1) % code_length
                count = 0
                while count < k:
                    new_code += temp_code[i]
                    i = (i + 1) % code_length
                    count += 1
            elif k < 0:
                i = idx - 1
                if i < 0:
                    i = code_length - 1
                count = 0
                while count < -k:
                    new_code += temp_code[i]
                    i -= 1
                    if i < 0:
                        i = code_length - 1
                    count += 1
            code[idx] = new_code
        return code


if __name__ == '__main__':
    Solution().decrypt()