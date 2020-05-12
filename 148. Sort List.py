# Mergesort in nlogn time.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            temp = slow
            slow = slow.next
        
        temp.next = None
        
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(slow)
        
        head = self.merge(left_sorted, right_sorted)
        return head
    
    def merge(self, l1, l2):
        head = ListNode(-1)
        h = head
        while l1 and l2:
            if l1.val<=l2.val:
                h.next = l1
                l1 = l1.next
            else:
                h.next = l2
                l2 = l2.next
            h = h.next
        
        while l1:
            h.next = l1
            l1 = l1.next
            h = h.next
            
        while l2:
            h.next = l2
            l2 = l2.next
            h = h.next
        return head.next