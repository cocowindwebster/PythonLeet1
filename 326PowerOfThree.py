class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: #ERROR1: Corner Case #1
            return False
        x = 1
        while x <= sys.maxsize / 3: # 1162261467 is 3^19, and 3^20 is larger than int
            x = x * 3
        print sys.maxsize, x
        return x % n == 0