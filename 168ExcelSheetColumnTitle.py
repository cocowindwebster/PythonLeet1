"""
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #NOTE1: ord('A') = 65
        #NOTE2: chr(ord('A') + 3) = 'D'
        result = ""
        while n > 0:
            n -= 1
            digit = n % 26
            result = chr(ord('A') + digit) + result
            n = n / 26
        return result

def main():
    s = Solution()
    print s.convertToTitle(32)


if __name__ == "__main__" :
    main()
