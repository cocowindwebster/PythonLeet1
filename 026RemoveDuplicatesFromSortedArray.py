class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, 1 #NOTE1: new way to initialize
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1  #NOTE2 Should left increment first or should update its value first? think thoroughly.
                nums[left] = nums[right]
            right += 1
        return left + 1  #NOTE3 The ending value
