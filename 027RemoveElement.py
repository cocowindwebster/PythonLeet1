class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = 0
        if nums == None or len(nums) == 0: #NOTE1: check 1 None, 2 len== 0
            return 0
        for right in xrange(0, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left