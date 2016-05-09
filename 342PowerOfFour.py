'''
0x55555555 = 0101 0101 0101 0101 0101 0101 0101 0101
reference: https://leetcode.com/discuss/97924/o-1-one-line-solution-without-loops
The basic idea is from power of 2, We can use "n&(n-1) == 0" to determine if n is power of 2. For power of 4, the additional restriction is that in binary form, the only "1" should always located at the odd position.
Solution2:  return num > 0 && (num & (num - 1)) == 0 && (num - 1) % 3 == 0
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0) and (num & (num - 1) == 0) and (num & 0x55555555 == num)
           