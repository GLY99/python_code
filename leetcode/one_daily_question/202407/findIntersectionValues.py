import collections

class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [0, 0]
        mapping1 = collections.defaultdict(int)
        mapping2 = collections.defaultdict(int)
        for num in nums1:
            mapping1[num] += 1
        for num in nums2:
            mapping2[num] += 2
            if mapping1.get(num, -1) != -1:
                ans[1] += 1
        for num in nums1:
            if mapping2.get(num, -1) != -1:
                ans[0] += 1
        return ans