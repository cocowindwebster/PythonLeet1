# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#ERROR1 TLE Intersected at '1': [1] [1]
#ERROR2 TLE Intersected at '3': [3] [2,3]
#ERROR3 No intersection: [1] [2,4,6,8,10,12,14,16,18,20,22] Output: Intersected at '8'  Expected: No intersection
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        if headA == headB: #ERROR1
            return headA
        previous = None
        current = headA
        while current != None:
            previous = current
            current = current.next
        previous.next = headB
        #fast = headA
        #slow = headB #ERROR2
        #slow = headB.next #ERROR3
        fast = headA
        #my preferred way is to "fast = head, slow= head"
        #some anaswers prefer "fast = head.next, slow= head".
        slow = headA
        meet = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                meet = fast
                break
        slow = headA
        if meet == None:
            previous.next = None # Recover the list structure
            return None
        else:
            while slow != fast:
                slow = slow.next
                fast = fast.next
            previous.next = None # Recover the list structure
            return fast
