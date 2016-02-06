# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_dummy = ListNode(1)
        even_head = even_dummy
        odd_dummy = ListNode(1)
        odd_head = odd_dummy
        switch = True
        while head:  #NOTE1: better than "while != None". In Python while, "true" is any non-zero value.
            if switch :
                odd_head.next = head
                odd_head = odd_head.next
                head = head.next
                odd_head.next = None #ERROR1: cut the Linkedlist to avoid loop
            else:
                even_head.next = head
                even_head = even_head.next
                head = head.next
                even_head.next = None
            switch = not switch
        odd_head.next = even_dummy.next
        return odd_dummy.next
