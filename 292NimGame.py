class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not (n % 5 == 0)


def main():
    s = Solution();
    print s.canWinNim(4);

if __name__ == "__main__" :
    main()
