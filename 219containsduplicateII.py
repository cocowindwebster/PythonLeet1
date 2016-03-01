"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the
array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
"""
#Solution 1
# key (the item )  -  value(list of all the index)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if nums == None or len(nums) == 0:
            return False
        dict = {}
        for i in range(len(nums)):
            item = nums[i]
            if dict.get(item, 0) == 0:
                dict[item] = [i]
            else:
                current_list = dict.get(item)
                if i - current_list[len(current_list) - 1] <= k:
                    return True;
                current_list.append(i)

        return False

"""

"""
#Solution 2
# key (the item )  -  value(a single value, most recent index)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if nums == None or len(nums) == 0:
            return False
        dict = {}
        for i in range(len(nums)):
            item = nums[i]
            if dict.get(item, -1) == -1:
                dict[item] = i
            else:
                if i - dict[item] <= k:
                    return True
                dict[item] = i
        return False
"""


#Soluiton 3
#same idea as Solution 2, more conside coding
#Solution 2
# key (the item )  -  value(a single value, most recent index)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None or len(nums) == 0:
            return False
        dict = {}
        # enumerate(iterable[, start]) -> iterator for index, value of iterable
        # enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
        for key, value in enumerate(nums):
            if dict.get(value, -1) != -1 and key - dict[value] <= k:
                return True
            dict[value] = key
        return False
