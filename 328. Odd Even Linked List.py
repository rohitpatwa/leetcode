# Take two pointers, even and odd. Keep moving them like (even.next = odd.next, odd.next = even.next). Merge two lists in the end

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        e0, o0 = head, head.next
        
        even = head
        odd = head.next
        
        while odd and even and odd.next:
            even.next = odd.next
            even = even.next
            odd.next = even.next
            odd = odd.next 
            
        if odd and even and odd.next:
            even.next = odd.next
            even = even.next
            odd.next = None
            even.next = o0
        
        elif odd and even and even.next!=odd:
            odd.next = even.next
            odd = odd.next
            even.next = o0
        else:
            even.next = o0
        return e0
            