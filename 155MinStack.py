
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if not self.stack_min :
            self.stack_min.append(x)
        #ERROR1:push(0),push(1),push(0),getMin,pop,getMin
        #elif x < self.stack_min[len(self.stack_min) - 1]:
        elif x <= self.stack_min[len(self.stack_min) - 1]:
            self.stack_min.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        current = self.stack.pop()
        if current == self.stack_min[len(self.stack_min) - 1]:
            self.stack_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[len(self.stack_min) - 1]
