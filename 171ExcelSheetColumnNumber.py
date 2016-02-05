class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for each in s:
            total = total * 26 + (ord(each) - ord('A')) + 1
            #NOTE1: built-in function ord() is to represent a unicode object to integer.
        return total;