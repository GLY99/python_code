class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(bits) - 2, -1, -1):
            if bits[i] != 1:
                break
            else:
                count += 1
        return count % 2 == 0