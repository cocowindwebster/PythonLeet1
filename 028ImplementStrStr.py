class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == None or haystack == "" or needle == None or needle == "":
            return -1
        i = 0
        while i < (len(haystack) - len(needle) +1):
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            if j == len(needle) :
                return i
            i += 1
        return -1;