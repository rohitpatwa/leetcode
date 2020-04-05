# Iterate on array from 1 to n. Wherever, arr[i] > arr[i-1], add it to profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	profit = 0
    	for i in range(1, len(prices)):
    		if prices[i] > prices[i-1]:
    			profit += prices[i] - prices[i-1]
    	return profit
