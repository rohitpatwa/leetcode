# l = len(s1). Slide over a window of size l on s2 and keep creating counters. If ctr_s1==ctr_s2: return true.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        if len(s2) < l:
            return False
        
        for i in range(len(s2) - l + 1):
            substr = s2[i:i+l]
            if Counter(s1) == Counter(substr):
                return True
        return False