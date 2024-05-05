class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i, num1 in enumerate(nums1):
            flag = False
            find = False
            for j, num2 in enumerate(nums2):
                if num1 == num2:
                    flag = True
                if flag and num2 > num1:
                    res.append(num2)
                    find = True
                    break
            if not find:
                res.append(-1)
        return res