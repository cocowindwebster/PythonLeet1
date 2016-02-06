class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = dict[s[len(s) - 1]]
        for i in range(len(s) - 2, -1, -1):
            if dict[s[i]] < dict[s[i + 1]]:
                number -= dict[s[i]]
            else:
                number += dict[s[i]]
        return number



def main():
    s = Solution();
    print s.romanToInt("VI");

if __name__ == "__main__" :
    main()
