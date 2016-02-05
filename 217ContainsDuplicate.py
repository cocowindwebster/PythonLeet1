# #Solution 1
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         dict = {}
#         for each in nums: # NOTE1: iterate through a list
#             print each
#             if dict.get(each, 0) == 0:
#                 dict[each] = 1
#             else:
#                 return True
#         return False

#Solution 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))