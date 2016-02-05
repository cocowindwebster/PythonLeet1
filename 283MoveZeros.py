#Solution 1: Not BRIEF ENOUGH
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         first = 0
#         second = 0
#         while  second < len(nums):
#             if nums[second] != 0:
#                 nums[first] = nums[second]
#                 first = first + 1
#             second = second + 1
#         while first < len(nums):
#             nums[first] = 0
#             first = first + 1

#Solution 2: Nice
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first = 0
        for second in range(len(nums)) :
            if nums[second]:  # write "if nums[second] != 0" as "if nums[second]" for short.
                nums[first], nums[second] = nums[second], nums[first] # exchange!
                first = first + 1
