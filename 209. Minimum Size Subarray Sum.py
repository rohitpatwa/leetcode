# Two pointer problem (i, j). Maintain a running sum and a left index (i). While running sum>target, sum-=arr[i] and i++; else sum+=arr[j], j++

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        left = 0
        res = 9999
        
        sum_val = 0
        
        for i in range(len(nums)):
            
            sum_val += nums[i]
        
            while sum_val >= s:
                res = min(res, i+1 - left)
                sum_val -= nums[left]
                left += 1
        
        return res if res!=9999 else 0
