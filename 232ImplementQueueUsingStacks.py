class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first = []
        self.second = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.first.append(x) #ERORR1: global name first is not defined


    def pop(self):
        """
        :rtype: nothing
        """
        #ERROR2: The IF Conditon should be testing the length of the list, not if the queue is None.
        #if self.second == None:
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.append(self.first.pop())
        if len(self.second) != 0:
            self.second.pop()


    def peek(self):
        """
        :rtype: int
        """
        #ERROR2: The IF Conditon should be testing the length of the list, not if the queue is None.
        #if self.second == None:
        if len(self.second) == 0:
            while len(self.first) != 0:
                self.second.append(self.first.pop())
        if len(self.second) != 0:
            return self.second[len(self.second) -1]
        else :
            return -1


    def empty(self):
        """
        :rtype: bool
        """
        #ERROR3
        #return len(self.first) != 0 and len(self.second) != 0
        return (self.first == None or len(self.first) == 0) and (self.second == None or len(self.second) == 0)
