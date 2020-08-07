# Sort intervals. Add first int(erval) to res. Iterate on remaining and check if curr[0] <= res[-1][1]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return []
        
        intervals = sorted(intervals)
        
        res = [intervals[0]]
        
        for i in intervals[1:]:
            prev_end = res[-1][1]
            
            curr_st, curr_end = i
            
            if curr_st <= prev_end:
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append(i)
        
        return res