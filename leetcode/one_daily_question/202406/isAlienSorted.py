class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        index = [0] * 26
        for idx, v in enumerate(order):
            index[ord(v) - ord('a')] = idx
        for i in range(len(words) - 1):
            flag = False
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if index[ord(words[i][j]) - ord('a')] > index[ord(words[i + 1][j]) - ord('a')]:
                    return False
                elif index[ord(words[i][j]) - ord('a')] < index[ord(words[i + 1][j]) - ord('a')]:
                    flag = True
                    break
            if not flag and len(words[i]) > len(words[i + 1]):
                return False
        return True

if __name__ == "__main__":
    Solution().isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz")