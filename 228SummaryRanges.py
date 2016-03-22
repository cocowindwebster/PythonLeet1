class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #ERROR1:
        #if nums == None:
        if nums == None or len(nums) == 0:
            return []
        first = nums[0]
        last = nums[0]
        result = []
        nums.append(nums[-1]) #sentinel
        for i in range(1, len(nums)):
            if nums[i] == last + 1:
                last = nums[i]
            else :
                if first != last:
                    each = str(first) + "->" + str(last)
                else:
                    each = str(first)
                result.append(each)
                first = nums[i]
                last = nums[i]
        return result
