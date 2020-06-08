# Do binary search until you find the mountain point.

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        
        while l<=r:
            m = (l+r)//2
            if A[m-1] > A[m]:
                r = m-1
            elif A[m+1] > A[m]:
                l = m+1
            else:
                return m
        return -1