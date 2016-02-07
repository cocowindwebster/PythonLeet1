# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n < 0:
#             return 0
#         elif n == 0 or n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else:
#             return self.climbStairs(n - 1) + self.climbStairs(n - 2) - 1 #ERROR1: Python Grammar is "self.classfunction"

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        dp = [1, 2]     #NOTE1: list initialization
        for i in xrange(3, n + 1, 1):
            i -= 1      #NOTE2: offset of 1, change 1-indexed to 0-indexed
            dp[i % 2] = dp[(i - 1) % 2] + dp[(i - 2) % 2]
        return dp[(n - 1) % 2]      #NOTE2: offset of 1, change 1-indexed to 0-indexed
