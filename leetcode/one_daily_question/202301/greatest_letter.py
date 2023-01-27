from string import ascii_lowercase, ascii_uppercase


class Solution:

    def __init__(self):
        super(self, Solution).__init__()

    def greatest_letter(self, s: str) -> str:
        """
        greatest letter
        :param s:
        :return:
        """
        letter_upper_list = [0] * 26
        letter_lower_list = [0] * 26
        for letter in s:
            if letter.islower():
                letter_lower_list[ord(letter) - 97] += 1
            else:
                letter_upper_list[ord(letter) - 65] += 1
        for i in range(25, -1, -1):
            if letter_lower_list[i] > 0 and letter_upper_list[i] > 0:
                return chr(i + ord('A'))
        return ""

    def greatest_letter(self, s: str) -> str:
        """
        greatest_letter
        :param s:
        :return:
        """
        for i in range(25, -1, -1):
            if ascii_uppercase[i] in s and ascii_lowercase[i] in s:
                return ascii_uppercase[i]
        return ""


if __name__ == '__main__':
    sol = Solution()
    s = "AAAa"
    print(sol.greatest_letter(s))

