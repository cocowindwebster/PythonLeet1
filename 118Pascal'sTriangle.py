class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
       """
        if not numRows or numRows < 1:
            #return [[]]   #ERROR: In think both "[[]]" or "[]" is fine
            return []
        result = [[1]]
        if numRows == 1:
            return result
        for i in range (1, numRows):
            current = [1]
            last = result[len(result) - 1]
            for j in range (1, i):
                current.append(last[j] + last[j - 1])
            current.append(1)
            result.append(current)
        return result
