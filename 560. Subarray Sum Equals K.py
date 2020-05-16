# Keep computing the cumsum and also store it's no. of occurances in a dict. For each cumsum, add d[cumsum-k] to result.

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        cumsum = 0
        d = {0:1}
        for i in nums:
            cumsum += i
            count += d.get(cumsum-k, 0)
            d[cumsum] = d.get(cumsum, 0) + 1
        return count