# Same as House Robber problem. This time we find max loot from [0:n-1] and [1:n] separately and return max of these.

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums) < 3:
            return max(nums)
        
        dp0 = [0]*(len(nums)-1)
        dp1 = [0]*(len(nums)-1)
        
        dp0[0] = nums[0]
        dp0[1] = max(nums[0], nums[1])
        
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])
        
        
        for i in range(2, len(nums)-1):
            dp0[i] = max(dp0[i-1], dp0[i-2] + nums[i])
            
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i+1])
        
        return max(dp0[-1], dp1[-1])
