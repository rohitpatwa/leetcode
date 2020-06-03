# Keep computing the cumsum and store it's no. of occurances in a dict. For each cumsum we get a k subarray if we've seen cumsum-k; result+= d.get[cumsum-k]

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # Initislize result, cumulative sum and dict storing the num occurances of cumsum
        # Start d with {0:1} because we have seen 0 once i.e. is in the beginning
        res, cumsum, d = 0, 0, {0:1}
        
        for i in nums:
            cumsum += i
            
            # if we have seen current cumsum-k, this means we have a subarray of sum k
            res += d.get(cumsum-k, 0)
            
            # add current cumsum to the dict
            d[cumsum] = d.get(cumsum, 0) + 1
        return res