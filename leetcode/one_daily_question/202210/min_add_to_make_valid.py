class Solution(object):

    @staticmethod
    def min_add_to_make_valid(s: str) -> int:
        """
        括号匹配问题（）））
        :param s:
        :return:
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        return len(stack)

    @staticmethod
    def min_add_to_make_valid(s: str) -> int:
        """
        括号匹配问题（）））
        :param s:
        :return:
        """
        ans = count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')' and count > 0:
                count -= 1
            else:
                ans += 1
        return count + ans

    @staticmethod
    def min_add_to_make_valid(s: str) -> int:
        """
        括号匹配问题（）））
        :param s:
        :return:
        """
        while "()" in s:
            s = s.replace("()", "")
        return len(s)
