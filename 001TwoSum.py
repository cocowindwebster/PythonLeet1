class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        dict = {}
        if nums == None or len(nums) == 0:
            return result
        for index in range(len(nums)):
            if target - nums[index] in dict:
                result.append(dict.get(target - nums[index]))
                result.append(index)
                #ERROR1 不能合并写，append()并不return the list
                #result.append(dict.get(target - nums[index])).append(index)
                return result
            else :
                dict[nums[index]] = index
        return result
