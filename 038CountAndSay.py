class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = "1"
        for i in range(n - 1):
            start = self.convert(start)
        return start
    def convert(self, str):
        if str == None or len(str) == 0:
            return ""
        i = 1
        first = str[0]
        count = 1
        result = ""
        while i < len(str): #?
            if str[i] == first:
                count += 1
            else :
                # ERROR1
                # I still don't know why I was getting error like this,
                # TypeError: 'str' object is not callable
                # but the fix is quite clear
                # result = result + str(count) + first
                result = "%s%d%s"%(result,count,first)
                first = str[i]
                count = 1
            i += 1
        # ERROR1
        # result = result + str(count) + first
        result = "%s%d%s"%(result,count,first)
        return result
