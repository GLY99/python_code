from queue import Queue


class Solution:
    def find_lex_smallest_string(self, s: str, a: int, b: int) -> str:
        """
        find lex smallest string
        """
        visited = set()
        q = Queue()
        q.put(s)
        visited.add(s)
        while not q.empty():
            cur_s = q.get()
            new_s = self.add_str(cur_s, a)
            if new_s not in visited:
                visited.add(new_s)
                q.put(new_s)
            new_s = self.overturn_str(cur_s, b)
            if new_s not in visited:
                visited.add(new_s)
                q.put(new_s)
        return sorted(visited)[0]
            

    def add_str(self, s: str, a: int) -> str:
        """
        add str
        """
        arr_s = list(s)
        for i in range(1, len(s), 2):
            new_c = int(arr_s[i]) + a
            arr_s[i] = str(new_c % 10) if new_c > 9 else str(new_c)
        return ''.join(arr_s)

    def overturn_str(self, s: str, b: int) -> str:
        """
        overturn str
        """
        length = len(s)
        return s[length - b: ] + s[: length - b]


if __name__ == '__main__':
    """
    main
    """
    obj = Solution()
    s = "5525"
    a = 9
    b = 2
    print(obj.find_lex_smallest_string(s, a, b))

