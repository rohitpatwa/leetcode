# Create a graph with all num-deno pairs. Perform BFS starting from each num until you find the deno.

from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}

        # Create the graph based on queries
        for i, (n, d) in enumerate(equations):
            if n in graph:
                graph[n][d] = values[i]
            else:
                graph[n] = {d: values[i]}

            if d in graph:
                graph[d][n] = 1/values[i]
            else:
                graph[d] = {n: 1/values[i]}

        # Initialize the result list
        res = []

        for n, d in queries:
            
            # If nuremrator or denominator is not in graph, return -1
            if n not in graph or d not in graph:
                res.append(-1)
                continue

            # If relationship is already present, return the value
            if d in graph[n]:
                res.append(graph[n][d])
                continue

            # Perform BFS on numerator's neighbors
            Q = deque(list(graph[n].keys()))
            while Q:
                curr = Q.popleft()
                for c in graph[curr]:
                    if c not in graph[n]:
                        val = graph[n][curr] * graph[curr][c]
                        graph[n][c] = val
                        graph[c][n] = 1/val # for future queries
                        Q.append(c)

                # Within each step of BFS, check if we found our d
                if d in graph[n]:
                    res.append(graph[n][d])
                    break

            # Even after completion of BFS, if we didn't find d, return -1
            if d not in graph[n]:
                res.append(-1)

        return res              
