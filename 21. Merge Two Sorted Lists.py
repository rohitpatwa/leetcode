# Merge part of merge sort

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val>=l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        
        temp = head
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            elif l1:
                temp.next = l1
                break
            else:
                temp.next = l2
                break
        return head