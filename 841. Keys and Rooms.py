# Do BFS on input. Maintin a set of (enqued + visited) rooms. Do not enque a room if it's there in the set.

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        q = [rooms[0]]
        enqued = set([0])
        
        while q:
            node = q[-1]
            q = q[:-1]
            
            for k in node:
                if k not in enqued:
                    q.append(rooms[k])
                    enqued.add(k)
        
        if len(enqued) == len(rooms):
            return True
        return False
    