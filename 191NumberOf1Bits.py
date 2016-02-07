class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:  #ERROR1: corner case
            return 0
        #count = 0   #ERROR2: should start from count = 1
        count = 1
        while n & (n - 1) != 0:
            count += 1;
            n = n & (n - 1)
        return count