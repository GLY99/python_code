class Solution:
    @staticmethod
    def score_of_parentheses(s: str) -> int:
        """
        给定一个平衡括号字符串S，按下述规则计算该字符串的分数：
        () 得 1 分。
        AB 得A + B分，其中 A 和 B 是平衡括号字符串。
        (A) 得2 * A分，其中 A 是平衡括号字符串。
        :param s:
        :return:
        """
        stack = [0]  # 初始化得分
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                cur = stack.pop()  # 遇到'）'弹出一个'（'的值
                if cur == 0:
                    stack.append(stack.pop() + 1)  # 最近的一次累加结果加上（）的值
                else:
                    stack.append(stack.pop() + 2 * cur)  # 最近的一次累加结果加上（A）的值
        return stack.pop()


if __name__ == "__main__":
    sol = Solution()
    s = "(()(()))"
    print(sol.score_of_parentheses(s))
