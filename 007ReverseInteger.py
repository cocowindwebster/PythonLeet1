class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0
        isPositive =True if x > 0 else False
        x = abs(x)
        result = 0
        while x > 0 :
            result = result * 10 + x % 10;
            x = x /10
        result = result if isPositive else -result
        return result if result < 2147483647 and result > -2147483648 else 0

    #Solution 2
    #def reverse(self, x):
        #return int(str(x)[::-1]) if x>=0 else -1*int(str(x)[1:][::-1])
