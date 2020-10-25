# Start with r=1. Keep doubling r until reader(r) > target. Perform Binary Search between r/2 and r.

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        r = 1
        while reader.get(r) < target:
            r *= 2
        
        l = r//2
    
        while l<=r:
            m = (l+r)//2
            arr_val = reader.get(m)
            if arr_val==target:
                return m
            elif arr_val < target:
                l = m+1
            else:
                r = m-1
        return -1