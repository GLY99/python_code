class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        res = [-1, -1]
        for i, num1 in enumerate(nums):
            find = False
            for j, num2 in enumerate(nums):
                if abs(i - j) >= indexDifference and abs(num1 - num2) >= valueDifference:
                    res[0] = i
                    res[1] = j
                    find = True
                    break
                if abs(j - i) >= indexDifference and abs(num2 - num1) >= valueDifference:
                    res[0] = j
                    res[1] = i
                    find = True
                    break
            if find:
                break
        return res
            