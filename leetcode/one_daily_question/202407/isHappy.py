class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, self.step(n)
        while fast != 1 and slow != fast:
            slow = self.step(slow)
            fast = self.step(self.step(fast))
        return fast == 1    

    def step(self, n):
        """
        step
        """
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n /= 10
        return sum