import collections

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ones_dict = collections.defaultdict(list)
        for num in arr:
            count = 0
            for s in str(bin(num)):
                if s == "1":
                    count += 1
            ones_dict[count].append(num)
        ans = []
        for i in range(15):
            if ones_dict[i]:
                ans += sorted(ones_dict[i])
        return ans