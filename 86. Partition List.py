# Initiate two lists for before and after, initiate them with ListNode(-1). Keep adding nodes to these lists. In the end, before.next = after_head.next; return before_head.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = ListNode(-1)
        after = ListNode(-1)
        before_head = before
        after_head = after
        
        
        while head:
            if head.val<x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next
                