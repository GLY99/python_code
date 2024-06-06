import collections

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        mapping = collections.defaultdict(int)
        for v in deck:
            mapping[v] += 1
        for x in range(2, len(deck) + 1):
            if len(deck) % x == 0:
                flag = True
                for _, v in mapping.items():
                    if v % x != 0:
                        flag = False
                if flag:
                    return True
        return False