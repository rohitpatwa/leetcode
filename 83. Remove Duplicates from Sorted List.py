# recurse on the linked list while ptr.next. store curr val. if next.val==curr, remove next; else val = next.val

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ptr = head
        
        val = ptr.val
        while ptr.next:
            if ptr.next.val==val:
                ptr.next = ptr.next.next
            else:
                val = ptr.next.val
                ptr = ptr.next
        return head