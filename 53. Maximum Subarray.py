# Create dp table of len(arr)+1. Initialize it to -inf. dp[i+1] = max(dp[i] + arr[i], arr[i]); return max(dp)


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-float('inf')]*(len(nums)+1)
        for i in range(len(nums)):
            dp[i+1] = max(dp[i] + nums[i], nums[i])
        return max(dp)