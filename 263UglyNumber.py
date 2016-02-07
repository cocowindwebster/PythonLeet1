class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while num > 0:
            if num % 2 == 0:
                num = num / 2;
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:              #ERROR1: should have a "break" for this else branch
                break
        return num == 1