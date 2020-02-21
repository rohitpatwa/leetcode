# Initiate two lists for before and after, initiate them with ListNode(0). Keep adding nodes to these lists. In the end, before.next = after_head.next; return before_head.next

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
        
        small = ListNode(0)
        small_ptr = small
        
        prev = ListNode(0)
        prev_ptr = prev 
        
        while head:
            if head.val < x:
                small_ptr.next = head
                small_ptr = small_ptr.next
                prev_ptr.next = head.next
            else:
                prev_ptr.next = head
                prev_ptr = head
            head = head.next

        small_ptr.next = prev.next
        return small.next


                