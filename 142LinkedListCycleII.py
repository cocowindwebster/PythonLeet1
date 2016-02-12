# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#ERROR1: [1] tail connects to node index 0
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        fast = head
        slow = head
        isCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                isCycle = True
                break;
        if not isCycle:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

