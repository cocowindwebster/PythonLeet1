class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""
        first = strs[0]
        i = 0
        for i in range(len(first)):
            for each in strs:
                if  i >= len(each) or each[i] != first[i]:
                        return first[0:i]
        return first