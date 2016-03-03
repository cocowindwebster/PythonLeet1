class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums == None :
            return
        current = 0
        self.sums = []
        for i in range(len(nums)) :
            current += nums[i]
            self.sums.append(current)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if j >= i and i >= 0 and j < len(self.sums):
            return self.sums[j] - self.sums[i - 1] if i > 0 else self.sums[j];
        return 0


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)