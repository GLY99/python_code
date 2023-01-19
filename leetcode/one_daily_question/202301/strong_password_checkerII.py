class Solution:
    def strong_password_checkerII(self, password: str) -> bool:
        """
        strong password checker II
        :param password:
        :return:
        """
        if len(password) < 8:
            return False
        lower_list = [chr(i + 97) for i in range(26)]
        upper_list = [chr(i + 65) for i in range(26)]
        num_list = [str(i) for i in range(10)]
        special_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
        res_list = [False] * 4
        for i in range(len(password)):
            if i != 0 and password[i] == password[i - 1]:
                return False
            if password[i] in lower_list:
                res_list[0] = True
                continue
            if password[i] in upper_list:
                res_list[1] = True
                continue
            if password[i] in num_list:
                res_list[2] = True
                continue
            if password[i] in special_list:
                res_list[3] = True
                continue
        return res_list[0] and res_list[1] and res_list[2] and res_list[3]