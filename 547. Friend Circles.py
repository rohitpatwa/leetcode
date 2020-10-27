# Keep a set of seen people. Now iterate on people from 1 to N, only those who are unseen. Do BFS on all it's unseen friends and mark all of them as seen.

from collections import deque

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = [False]*len(M)
        connected_components = 0
        
        for i in range(len(M)):
            if not seen[i]:
                connected_components += 1
                Q = deque([i])
                while Q:
                    curr = Q.popleft()
                    for j, val in enumerate(M[curr]):
                        if val and not seen[j]:
                            seen[j] = True
                            Q.append(j)
                            
        return connected_components