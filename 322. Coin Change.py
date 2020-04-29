# dp = ['Inf'] *(amount+1);dp[0]=0;iterate over the table and iterate over all possible coins(nested). dp[amt] = min(dp[amt], dp[amt - coin] + 1)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Create a DP table of size (amount + 1)
        dp = [float('Inf')] *(amount+1)
        
        # Initiate dp[0] (to reach amount 0, we need 0 coins)
        dp[0] = 0
        
        # iterate over coins
        for amt in range(amount+1):
            for coin in (coins):
            # iterate over amounts bigger than coin value
                # min (existing val of table, reqd val - coin val + 1)
                # Basically deciding whether to pick this coin or not to reach 
                # that value on optimum no. of coins
                if amt>=coin:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        # return if we were able to reach the desired amount.
        return dp[-1] if dp[-1] != float('Inf') else -1
