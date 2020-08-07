# Assign +1 -1 values to "NSEW". Use cartesian coordinates and store values in a set. If value repeated, return True.

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        if not path: return False
        
        x, y = 0, 0 
        
        visited = set()
        
        for p in path:
            visited.add((x,y))
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'E':
                x += 1
            else:
                x -= 1
            
            if (x,y) in visited:
                return True
        return False
        