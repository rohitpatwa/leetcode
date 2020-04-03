# Find the lengths of the two ll. Move the head of larger ll by l1-l2 steps. Then move both heads and compare at step.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def len(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n1 = self.len(headA)
        n2 = self.len(headB)
        
        if n1>n2:
            for _ in range(n1-n2):
                headA = headA.next
        elif n2>n1:
            for _ in range(n2-n1):
                headB = headB.next
        
        while headA:
            if headA==headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
                