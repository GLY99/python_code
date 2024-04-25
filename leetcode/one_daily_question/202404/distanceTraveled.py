class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        if mainTank < 5:
            return mainTank * 10
        res = 0
        while mainTank >= 5:
            mainTank -= 5
            res += 50
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        res += mainTank * 10
        return res