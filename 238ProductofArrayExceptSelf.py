class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if nums == None or len(nums) == 0:
            return result
        left, right = 1, 1
        result = [1] * len(nums)
        for i in range (0, len(nums)):
            result[i] *= left
            result[len(nums) - i - 1] *= right
            left *= nums[i]
            right *= nums[len(nums) - i - 1]
        return result
