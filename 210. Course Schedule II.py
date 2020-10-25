# Same as Course Schedule problem. Create a res list to store resut. When popping from Stack, add to res.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        graph = defaultdict(list)
        
        res = []
        
        for p in prerequisites:
            inDegree[p[0]] += 1
            graph[p[1]].append(p[0])
            
        Q = []
        
        for i,x in enumerate(inDegree):
            if x==0:
                Q.append(i)
                
        while Q:
            curr = Q.pop(0)
            res.append(curr)
            for dependent in graph[curr]:
                inDegree[dependent] -= 1
                if inDegree[dependent]==0:
                    Q.append(dependent)
                    
        if sum(inDegree)==0:
            return res
        return []
                