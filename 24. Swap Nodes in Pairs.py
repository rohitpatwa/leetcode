# Take next two nodes, swap them and chage pointers, jump two steps from current.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        curr = ListNode(0)
        res = curr
        curr.next = head
        
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            temp = node2.next
            
            curr.next = node2
            node2.next = node1
            node1.next = temp
            curr = node1
        return res.next
        
        
#         res = head.next
#         prev = None
#         while head and head.next:
#             node1 = head
#             node2 = head.next
#             temp = node2.next
            
#             node2.next = node1
#             node1.next = temp
            
#             if prev:
#                 prev.next = node2
#             prev = node1
#             head = node1.next
#         return res
        