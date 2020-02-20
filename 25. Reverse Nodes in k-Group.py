# Keep reversing k chunks of linked list. Maintin the tail of previos chunk to point to the next reversed chunk's head.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return self.helper(head, k)
        
    def helper(self, head, k):
        
        prev_tail = None
        flag, flag2 = True, True
        res = head

        while head:
            
            # Check if there are k more nodes in list
            ptr = head
            for j in range(k):
                if ptr:
                    ptr = ptr.next
                else:
                    flag2 = False
            
            
            i = 0
            og_head = head
            prev = None

            # flag2 True means there are k more nodes in list 
            if flag2:
                while i<k:
                    _next = head.next
                    head.next = prev
                    prev = head
                    head = _next
                    i += 1
            else:
                # len of remaining list < k
                if prev_tail:
                    prev_tail.next = head
                break
            
            if prev_tail:
                prev_tail.next = prev
            
            prev_tail = og_head
            
            if flag:
                # flag is to mark the overall head of the list
                res = prev
                flag = False
        return res