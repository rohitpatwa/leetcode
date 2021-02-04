# Create dp table of len(arr). Initialize it to 0. dp[i] = max(dp[i-1] + arr[i], arr[i]); return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        dp = [nums[0]]*len(nums)
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
            
        return max(dp)



#Kadane's Algorithm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            s = max(nums[i], s+nums[i]) # This is the key step
            global_max = max(global_max, s)
        return global_max