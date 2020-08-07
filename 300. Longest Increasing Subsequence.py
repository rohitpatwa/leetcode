# DP problem, O(n^2). Initiate lis=[1]*n. If A[i]>A[j] and lis[j]>=lis[i]: lis[i] = lis[j] + 1.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        dp = [1]*len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
                    
        return max(dp)
                    