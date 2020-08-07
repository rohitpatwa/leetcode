# At each element, keep track of min and max because in products, min can become max if multiplied by -ve no.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_p, max_p, res = nums[0], nums[0], nums[0]
        
        for i in nums[1:]:
            max_p, min_p = max(min_p*i, max_p*i, i), min(min_p*i, max_p*i, i)
             
            res = max(max_p, res)
            
        return res