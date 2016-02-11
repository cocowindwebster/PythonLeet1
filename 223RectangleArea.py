
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rightX, rightY = min(C, G), min(D,H)
        leftX, leftY = max(A, E), max(B,F)
        #ERROR1 corner case: if there is no overlap
        #sum = (C-A) * (D-B) + (G-E)*(H-F) - (rightX - leftX) * (rightY - leftY)
        if rightX < leftX or rightY < leftY:
            sum = (C-A) * (D-B) + (G-E)*(H-F)
        else:
            sum = (C-A) * (D-B) + (G-E)*(H-F) - (rightX - leftX) * (rightY - leftY)
        return sum