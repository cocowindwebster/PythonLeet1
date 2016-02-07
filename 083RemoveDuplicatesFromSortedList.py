# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy_head = ListNode(head.val - 1);
        tail = dummy_head
        while head != None:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
            tail.next = None #ERROR1:Break the chain
        return dummy_head.next