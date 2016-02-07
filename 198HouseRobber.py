class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in xrange(2, len(nums), 1):
            dp[i % 2] = max(dp[(i - 2) % 2] + nums[i], dp[(i - 1) % 2])
        return dp[(len(nums) - 1) % 2]
