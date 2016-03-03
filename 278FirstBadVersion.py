# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#ERROR1: TLE 2 versions  2 is the first bad version.
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left + 1 < right:
            mid = left + (right - left) / 2;
            if isBadVersion(mid) :
                # right = mid - 1
                right = mid
            else :
                left = mid + 1
        if isBadVersion(left) :
            return left
        elif isBadVersion(right) :
            return right
        else :
            return 0