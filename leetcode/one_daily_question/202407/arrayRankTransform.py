import copy
import collections


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        tmp_arr = copy.deepcopy(arr)
        tmp_arr = sorted(tmp_arr)
        mapping = collections.defaultdict(int)
        for idx, num in enumerate(tmp_arr):
            if not mapping.get(num, None):
                mapping[num] = len(mapping) + 1
        ans = []
        for idx, num in enumerate(arr):
            ans.append(mapping[num])
        return ans