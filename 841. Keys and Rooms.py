# Do DFS on input. Maintin a set of keys_collected. Do not push a room if it's there in the keys_collected set.

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        S = [rooms[0]]
        keys_collected = set([0])
        
        while S:
            node = S.pop()
            
            for k in node:
                if k not in keys_collected:
                    S.append(rooms[k])
                    keys_collected.add(k)
        
        if len(keys_collected) == len(rooms):
            return True
        return False
    