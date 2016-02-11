class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()

        #ERROR1 NOTE Recommend because both the tuple and the condition will be evaluated, error-prone.
        #return (len(list[len(list) - 1]), 0) [list == []]
        return len(s.split()[len(s.split())-1]) if s.split() != [] else 0