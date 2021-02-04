# Check the diff between consecutive elements of nums. If it's > 1, send it to format function. Add edge cases separately.

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def format(a, b, res):
            if a==b:
                res.append(str(a))
            elif b>a:
                res.append(f'{a}->{b}')
        
        res = []
        if not nums:
            format(lower, upper, res)
            return res        

        format(lower, nums[0]-1, res)

        for i in range(1, len(nums)):
            format(nums[i-1]+1, nums[i]-1, res)

        format(nums[-1]+1, upper, res)
        
        return res