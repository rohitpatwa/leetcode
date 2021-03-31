# Find total no. of connected_components by performing Perform DFS on each unvisited stone and add it's neighbors to visoted set.

from collections import deque

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        connected_components = 0
        rows, cols = {}, {}
        
        for i, s in enumerate(stones):
            rows[s[0]] = rows.get(s[0], []) + [i]
            cols[s[1]] = cols.get(s[1], []) + [i]
            stones[i] = tuple(s)
            
        visited = set()
        
        for s in stones:
            if s not in visited:
                connected_components += 1
                Q = deque([s])
                
                while Q:
                    curr = Q.popleft()
                    if curr not in visited:
                        visited.add(curr)
                        
                        for stone in rows[curr[0]]:
                            Q.append(stones[stone])
                        for stone in cols[curr[1]]:
                            Q.append(stones[stone])
        
        return len(stones) - connected_components