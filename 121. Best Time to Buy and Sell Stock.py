# Iterate through the array and maintain the min_so_far value. at each step profit = max(profit, arr[i]-min_so_far)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        min_so_far = 99999
        
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-min_so_far)
            min_so_far = min(min_so_far, prices[i])
            
        return max_profit