# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#ERROR1: corner case 1, if the input list has only one node, then return should be None
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or (head.next == None and n == 1):
            return None
        dummyNode = ListNode(-1)
        dummyNode.next = head
        head = dummyNode
        # [1, 2, 3, 4, 5]   -> add dummy node -1 ->  [-1, 1, 2, 3, 4, 5]
        fast = head
        while n > 0:
            if fast == None:
                return head;
            else:
                fast = fast.next;
            n -= 1;
        slow = head;
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
        if slow.next != None:
            slow.next = slow.next.next
        return dummyNode.next
