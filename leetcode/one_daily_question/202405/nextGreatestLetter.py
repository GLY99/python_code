class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        length = len(letters)
        left = 0
        right = length - 1
        if target >= letters[right]:
            return letters[0]
        while left < right:
            mid = (left + right) / 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        return letters[left]