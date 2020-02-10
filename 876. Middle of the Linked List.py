# Use slow pointer, fast pointer approach

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            
        return head
