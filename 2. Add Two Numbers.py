# Iterate over 2 LL. Maintain carry digit. Keep adding new nodes to res. In the end, check if carry is set.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = ListNode(-1)
        out_head = out
        ptr1, ptr2 = l1, l2
        c = 0
        
        while ptr1 or ptr2:
            v1, v2 = ptr1.val if ptr1 else 0, ptr2.val if ptr2 else 0
            out.next = ListNode((v1+v2+c)%10)
            out = out.next
            c = (v1+v2+c)//10
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        if c:
            out.next = ListNode(1)
        return out_head.next