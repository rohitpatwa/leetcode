# Place two pointers n nodes apart in the linked list. As ptr1 reaches the end, ptr2 will be on the nth node from end.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        temp = ListNode(-1)
        temp.next = head
        ptr1 = ptr2 = temp
        
        while n and ptr2:
            ptr2 = ptr2.next
            n -= 1
        
        while ptr2 and ptr2.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        ptr1.next = ptr1.next.next
        return temp.next



## Recursive solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.n=n
        temp = ListNode(-1)
        temp.next = head
        self.helper(temp)
        return temp.next
    
    def helper(self, node):
        if node is None:
            return -1
        count = self.helper(node.next) + 1
        if count == self.n:
            node.next = node.next.next
        return count
            