# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head;
        dummyHead = ListNode(-1)
        dummyTail = dummyHead
        first = head
        second = head.next
        third = None
        while first != None and second != None:
            third = second.next
            dummyTail.next = second
            dummyTail = dummyTail.next
            dummyTail.next = first
            dummyTail = dummyTail.next
            dummyTail.next = None
            first = third
            if first != None:
                second = first.next
        if second == None:
            dummyTail.next = first
        return dummyHead.next

