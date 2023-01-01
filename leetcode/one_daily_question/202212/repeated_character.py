class Solution(object):
    def repeated_character(self, s: str) -> str:
        """
        repeated character
        :param s:
        :return:
        """
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
            if char_map.get(c, 0) >= 2:
                return c