# One pass solution. At each num, if it's seen before n times, increment res by n. Then increment d[num] by 1.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        res = 0
        
        for j, x  in enumerate(nums):
            
            past = d.get(x, 0)
            res += past
                        
            d[x] = past + 1
            
        return res