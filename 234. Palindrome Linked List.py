# Use fast & slow pointers. Take fast pointer to end, slow pointer will be in the middle. Reverse ll ahead of slow pointer and initiate fast pointer to head. Compare.


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
        slow = head
        fast = head
        
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        
        slow = self.reverse(slow)
        fast = head
        
        
        while slow != None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
        
        
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev