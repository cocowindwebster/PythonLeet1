class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None:
            return True
        stack = []
        for each in s:
            if each == '(' or each == '[' or each == '{':
                stack.append(each)
            elif each == ')' :
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] != '(':
                    return False
                elif stack[len(stack) - 1] == '(':
                    stack.pop()
            elif each == '}':
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] != '{':
                    return False
                elif stack[len(stack) - 1] == '{':
                    stack.pop()
            elif each == ']':
                if len(stack) == 0:
                    return False
                elif stack[len(stack) - 1] != '[':
                    return False
                elif stack[len(stack) - 1] == '[':
                    stack.pop()
            else:
                return False
        return len(stack) == 0