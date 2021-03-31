# Create a left and right array to hold the max profit in left and right dir. Iterate from start to end on left and reverse on right array.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        left, right = [0]*len(prices), [0]*len(prices)
        left_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < left_min:
                left_min = prices[i]
                left[i] = left[i-1]
            else:
                left[i] = max(left[i-1], prices[i] - left_min)
                
        right_max = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > right_max:
                right_max = prices[i]
                right[i] = right[i+1]
            else:
                right[i] = max(right[i+1], right_max - prices[i])
                
        res = 0
        for i in range(len(prices)):
            res = max(res, left[i] + right[i])
        return res


# Maintain 4 vars, t1_cost, t2_cost, t1_profit, t2_profit. Iterate through the prices once and try to minimize cost and maximize profit. Return t2_profit.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0
        
        for i in range(len(prices)):
            t1_cost = min(t1_cost, prices[i])
            t1_profit = max(t1_profit, prices[i] - t1_cost)
            t2_cost = min(t2_cost, prices[i] - t1_profit)
            t2_profit = max(t2_profit, prices[i] - t2_cost)
        
        return t2_profit