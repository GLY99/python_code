class Solution:
    def check_self_palindrome(self, str1: str, left: int, right: int):
        """
        check self palindrome
        """
        while left < right and str1[left] == str1[right]:
            left += 1
            right -= 1
        return left >= right

    def check_concatenation(self, str1: str, str2: str) -> bool:
        """
        check concatenation
        """
        left = 0
        right = len(str1) - 1
        while left < right and str1[left] == str2[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return self.check_self_palindrome(str1, left, right) or self.check_self_palindrome(str2, left, right)

    def check_palindrome_formation(self, a: str, b: str) -> bool:
        """
        check palindrome formation
        :params a: str
        :params b: str
        """
        return self.check_concatenation(a, b) or self.check_concatenation(b, a)
        
