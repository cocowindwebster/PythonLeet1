class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None:
            return ""
        else:
            return s[::-1]