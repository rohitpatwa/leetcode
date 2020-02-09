# dp = ['Inf'] *(amount+1);dp[0]=0;iterate over the table and iterate over all possible coins(nested). dp[amt] = min(dp[amt], dp[amt - coin] + 1)
