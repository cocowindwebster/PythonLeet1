# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True;
        # 1 find mid point
        fast = head.next
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        second_head = slow.next
        slow.next = None
        # 2 reverse() and compare, the trick is that reversing the second part will work better
        new_second_head = self.reverse(second_head)
        while head != None and new_second_head != None:
            if head.val != new_second_head.val:
                return False
            head, new_second_head = head.next, new_second_head.next
        # 3 recover
        second_head = self.reverse(new_second_head)
        slow.next = second_head
        return True

    def reverse(self, head):
        previous = None
        current = head
        next = None
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
