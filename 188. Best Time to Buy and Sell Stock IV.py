# Create intervals. Calculate 2 lossed, merge loss and remove loss. If remove loss <= merge loss, remove that int, else merge those 2 adj intervals.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if not k or not prices:
            return 0
        
        n = len(prices)
        transactions = 0
        profit = 0
        intervals = []
        
        # Create intervals
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                transactions += 1
                intervals.append([i-1, i])
                profit += prices[i] - prices[i-1]
        
        if transactions <= k:
            return profit
        
        if not intervals:
            return 0
        
        S = [intervals[0]]
        
        # merge the intervals
        for i in intervals[1:]:
            if i[0] == S[-1][1]:
                S[-1][1] = i[1]
                transactions -= 1
            else:
                S.append(i)
                
            if transactions <= k:
                return profit
            
        intervals = S
        
        # repeatedly remove/merge the least profitable interval
        while transactions > k:
            
            min_delete_loss = float('inf')
            min_delete_idx = None
            for i in range(len(intervals)):
                loss = prices[intervals[i][1]] - prices[intervals[i][0]]
                if loss < min_delete_loss:
                    min_delete_loss = loss
                    min_delete_index = i
                    
            min_merge_loss = float('inf')
            min_merge_index = None
            for i in range(1, len(intervals)):
                loss = prices[intervals[i-1][1]] - prices[intervals[i][0]]
                if loss < min_merge_loss:
                    min_merge_loss = loss
                    min_merge_index = i
                    
            if min_delete_loss <= min_merge_loss:
                profit -= min_delete_loss
                intervals.pop(min_delete_index)
            else:
                profit -= min_merge_loss
                popped_interval = intervals.pop(min_merge_index)
                intervals[min_merge_index-1][1] = popped_interval[1]    
            transactions -= 1
            
        return profit




# Crete a 3D dp array. D1=days, D2=transactions, D3=[Sell, Buy]. Return dp[-1][-1][0]

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not k or not prices:
            return 0
        
        n = len(prices)
        
        if k >= n-1:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i-1])
            return res
        
        # Initialize the dp array with [no-stock, stock] status.
        # DP holds the max profit in each cell
        dp = [[[0, -prices[0]] for x in range(k+1)] for y in range(n)]
        
        for i in range(1, n):
            for j in range(1, k+1):
                # Choose the max between hold(do nothing) and sell(already have stock)
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                
                # Choose the max between hold(do nothing) and buy(have no stock already)
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        return dp[-1][-1][0]