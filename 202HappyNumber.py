class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while n > 0:
            sum = 0
            while n > 0:
                sum += (n % 10) * (n % 10)
                n = n / 10
            if sum == 1:
                return True
            elif dict.get(sum, 0) != 0:
                return False
            else:
                dict[sum] = 1
            n = sum