# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Solution 1
"""
class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return head
        dummy_head= ListNode(-1)
        dummy_tail = dummy_head
        while head != None:
            if head.val != val:
                dummy_tail.next = head
                dummy_tail = dummy_tail.next
                head = head.next
                dummy_tail.next = None
            else:
                head = head.next
        return dummy_head.next
"""

# Solution 2
# after condensing the code from Solution 1
class Solution(object):
    def removeElements(self, head, val):
        if head == None:
            return head
        dummy_head= ListNode(-1)
        dummy_tail = dummy_head
        while head != None:
            if head.val != val:
                dummy_tail.next = head
                dummy_tail = dummy_tail.next
            head = head.next
        dummy_tail.next = None
        return dummy_head.next
