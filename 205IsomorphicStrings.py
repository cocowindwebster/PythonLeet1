class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}
        if  s == None or t == None:
            return True
        for i in range(len(s)):
            alpha = s[i]
            beta = t[i]
            if dict1.get(alpha, 0) == 0:
                dict1[alpha] = t[i]
            elif t[i] != dict1[alpha]:
                return False
            if dict2.get(beta, 0) == 0:
                dict2[beta] = s[i]
            elif s[i] != dict2[beta]:
                return False
        return True
