class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #ERROR1: validate k,
        if nums == None or k == 0 or k % len(nums) == 0:
            return
        k = k % len(nums)
        nums.reverse()
        #nums[0:k] = list(nums[0:k].reverse())
        #NOTE1: nums[::-1] sliceint returns a copy
        #NOTE2: reverse is inplace operation, equivalent to a void return type funciton
        first, second = nums[0:k], nums[k:]
        first.reverse()
        second.reverse()
        nums[0:k], nums[k:] = first,second