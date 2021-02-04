# Find len of ll. k = k%l. Then mode l-k-1 steps and break the ll. Add the remaining part of the LL in the front.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        
        l, ptr = 0, head

        while ptr:
            l += 1
            ptr = ptr.next
            
        if l==0 or k%l==0:
            return head
        k = k % l
        
        
        ptr = head
        for _ in range(l-k-1):
            ptr = ptr.next
        
        new_head = ptr.next 
        ptr.next = None
        
        ptr = new_head
        while ptr.next:
            ptr = ptr.next
        ptr.next = head
        
        return new_head