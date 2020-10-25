# Create list of inDegree(iD) of edges and DAG. Add nodes with iD==0 to Stack(S). Pop S, decrease inDegree of dependents by 1. If iD==0, push to S.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        inDegree = [0]*numCourses
        
        
        # [0, 1] => 0 is course and 1 is prereq
        
        for u, v in prerequisites:
            inDegree[u] += 1
            graph[v].append(u)  # DAG = 1 -> 0
            
        S = []  # can be done with Q also
        # Q = []  # can be done with S also
        
        # Append courses with 0 prereq to stack/queue
        for i in range(len(inDegree)):
            if inDegree[i]==0:
                S.append(i)
        
        while S:
            curr = S.pop()
            for dependent in graph[curr]:
                inDegree[dependent] -= 1

                if inDegree[dependent] == 0:
                    S.append(dependent)
                    
        return sum(inDegree)==0
                