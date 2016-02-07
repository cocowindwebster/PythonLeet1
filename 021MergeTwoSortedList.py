# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        tail = dummyNode
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            tail.next = None
        if l1 != None:
            tail.next = l1
        if l2 != None:
            tail.next = l2
        return dummyNode.next