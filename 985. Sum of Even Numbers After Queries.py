# Keep a running sum. At each query, subtract the initial term if even and add the new term if even. Append sum in results.

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        for x in A:
            if x%2==0:
                s += x
        res = []
        for (x, i) in queries:
            if A[i]%2==0:
                s -= A[i]
            
            A[i] += x
            
            if A[i]%2==0:
                s += A[i]
            
            res.append(s)
        return res