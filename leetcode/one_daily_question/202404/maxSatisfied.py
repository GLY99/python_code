class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        count = 0
        for i, val in enumerate(customers):
            if grumpy[i] == 0:
                count += val
        
        increase = 0
        for i, val in enumerate(customers):
            if i >= minutes:
                break
            increase += customers[i] * grumpy[i]
        
        maxIncrease = increase
        i = minutes
        while i < len(customers):
            increase = increase - customers[i - minutes] * grumpy[i - minutes] + customers[i] * grumpy[i]
            maxIncrease = max(increase, maxIncrease)
            i += 1
        return count + maxIncrease