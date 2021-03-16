# Use prev and next as extra variables. while h: [n=h.n; h.n=p; p=h; h=n]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


# Recursive approach. Compute new head once and return that in every call. Head.next.next = head.
class Solution:
    def reverseList(self, head):  # Recursive

        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head 