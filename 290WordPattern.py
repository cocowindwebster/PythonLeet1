# ERROR1: Line 27: IndexError: string index out of range
# "aaa"
# "aa aa aa aa"

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        if pattern == None and str == None:
            return True;
        if pattern == None or str == None:
            return False;

        splitted = str.split(' ')

        dict1 = {}
        for i in range(len(pattern)) :
            if i >= len(splitted):  #ERROR1
                return False
            elif dict1.get(pattern[i], 0) == 0:
                dict1[pattern[i]] = splitted[i]
            elif dict1[pattern[i]] != splitted[i]:
                return False

        dict2 = {}
        for i in range(len(splitted)) :
            if i >= len(pattern):   #ERROR1
                return False
            elif dict2.get(splitted[i], 0) == 0:
                dict2[splitted[i]] = pattern[i]
            elif dict2[splitted[i]] != pattern[i]:
                return False
        return True