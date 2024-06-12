class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        r = purchaseAmount % 10
        if r < 5:
            purchaseAmount -= r
        else:
            purchaseAmount += 10 - r
        return 100 - purchaseAmount