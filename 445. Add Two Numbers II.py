# Find len of two linked lists. Pad shorter one with 0s. Call them recursively. When end is reached, keep adding the elements and maintain the carry bit.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        len1, len2 = self.length(l1), self.length(l2)
        
        if len1>len2:
            l2 = self.pad(l2, len1-len2)
        else:
            l1 = self.pad(l1, len2-len1)
        
        self.res = ListNode(-1)
        self.c = 0
        
        self.add(l1, l2)
        
        if self.c:
            temp = ListNode(1)
            temp.next = self.res.next
            self.res.next = temp

        return self.res.next
    
    def add(self, l1, l2):
        
        if l1.next and l2.next:
            self.add(l1.next , l2.next)
        temp = ListNode((l1.val + l2.val + self.c)%10)
        temp.next = self.res.next
        self.res.next = temp
        self.c = (l1.val + l2.val + self.c)//10
    
    
    def length(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l
    
    
    def pad(self, node, k):
        for _ in range(k):
            n = ListNode(0)
            n.next = node
            node = n
        return node
                