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