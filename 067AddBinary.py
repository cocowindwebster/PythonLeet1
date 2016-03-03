#ERROR1: Input: "0", "0"   Output: "00"    Expected: "0"
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == None or a == "":
            return b
        elif b == None or b == "":
            return a
        a = a[::-1]
        b = b[::-1]
        diff = '0' * abs(len(a) - len(b))
        if len(a) < len(b):
            a = a + diff
        else :
            b = b + diff
        sum = ''
        carry = 0;
        for i in range(len(a)):
            current =  (carry + (ord(a[i]) - ord('0'))  +  (ord(b[i]) - ord('0')))
            sum = sum + str(current % 2)
            carry = current / 2
        # ERROR1
        # should not omit this if condition, else ERORR 1
        if carry > 0:
            sum += str(carry)
        return sum[::-1]



        