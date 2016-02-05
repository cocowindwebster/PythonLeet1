class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for each in s:
            dict[each] = dict.get(each, 0) + 1
        for each in t:
            dict[each] = dict.get(each, 0) - 1
            if dict[each] < 0:
                return False
        for k, v in dict.items():
            if v:
                return False;
        return True;