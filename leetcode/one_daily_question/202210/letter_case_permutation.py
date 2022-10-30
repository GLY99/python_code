from typing import List
from collections import deque


class Solution:
    def letter_case_permutation(self, s: str) -> List[str]:
        """
        :param s:
        :return:
        """
        ans_list = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                tmp_ans_list = []
                for s1 in ans_list:
                    tmp_s = s1[0:]
                    tmp_arr = list(tmp_s)
                    if s[i].islower():
                        tmp_arr[i] = s[i].upper()
                        tmp_ans_list.append(''.join(tmp_arr))
                    else:
                        tmp_arr[i] = s[i].lower()
                        tmp_ans_list.append(''.join(tmp_arr))
            else:
                continue
            ans_list += tmp_ans_list
        return ans_list

    def letter_case_permutation(self, s: str) -> List[str]:
        """
        :param s:
        :return:
        """
        ans_list = []
        length = len(s)

        def dfs(idx, cur_s):
            if idx == length:
                ans_list.append(cur_s)
                return
            dfs(idx + 1, cur_s + s[idx])
            if 'a' <= s[idx] <= 'z' or 'A' <= s[idx] <= 'Z':
                dfs(idx + 1, cur_s + s[idx].swapcase())

        dfs(0, '')
        return ans_list

    def letter_case_permutation(self, s: str) -> List[str]:
        """
        :param s:
        :return:
        """
        ans_list = []
        length = len(s)
        q = deque()
        q.append('')
        while q:
            cur = q[0]
            pos = len(cur)
            if pos == length:
                ans_list.append(cur)
                q.popleft()
            else:
                if s[pos].isalpha():
                    q.append(cur + s[pos].swapcase())
                q[0] += s[pos]
        return ans_list


if __name__ == "__main__":
    sol = Solution()
    s = "a1b2"
    print(sol.letter_case_permutation(s))
