class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        result = 0
        old_x = x
        while x > 0:
            result = result * 10 + x % 10
            x = x /10
        print old_x, result
        return old_x == result
