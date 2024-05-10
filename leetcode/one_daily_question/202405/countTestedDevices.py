class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        count = 0
        length = len(batteryPercentages)
        for i, batteryPercentage in enumerate(batteryPercentages):
            if batteryPercentage > 0:
                count += 1
                for j in range(i+1, length):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return count