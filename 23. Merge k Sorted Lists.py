# Use min heap of size k. Add 1 elem from each list in format (val, i++, next_ptr). i is added to allow heap sorting. Pop from heap and add from same list.


import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = ListNode(-1)
        ptr = res
        
        l = []
        i = 0        
        for k in lists:
            if k:
                heapq.heappush(l, (k.val, i, k))
                i += 1
            
        while l:
            val, _, node = heapq.heappop(l)
            ptr.next = node
            ptr = ptr.next
            
            if node.next:
                heapq.heappush(l, (node.next.val, i, node.next))
                i += 1
        ptr.next = None
        return res.next