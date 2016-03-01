"""Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
"""

"""
# Solution 1(Incorrect)
# incorrect : since the prevailing 0 will be incorrectly discarded during the conversion. Note the questions
    has already specified the problem to be a 32 bits unsigned integer.
# e.g. 42361596 -> 15065253
# 00000010100101000001111010011100 -> 111001011110000010100101
class Solution(object):
    def reverseBits(self, n):
        res = 0
        while  n != 0 :
            res = (res << 1) | (n & 1)
            n = n >> 1
            print "{0:b}".format(n), "-", "{0:b}".format(res)
        return res
"""

class Solution(object):
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
            # NOTE1: print bitwise representation
            # print "{0:b}".format(n), "-", "{0:b}".format(res)
        return res

def main ():
    solution = Solution()
    print "{0:b}".format(43261596)
    reversed = solution.reverseBits(43261596)
    print "{0:b}".format(reversed)
    print reversed

if __name__ == "__main__" :
    main()


