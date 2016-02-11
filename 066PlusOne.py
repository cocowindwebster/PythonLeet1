class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits) - 1] += 1
        result = []
        carry = 0
        for digit in digits[::-1]:
            current = (carry + digit) % 10
            carry = (carry + digit) / 10
            result.append(current)
        if carry != 0:
            result.append(carry)
        return result[::-1]
