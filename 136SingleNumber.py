class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None :
            return 0
        x = 0
        for each in nums:
            x = x ^ each
        return x
