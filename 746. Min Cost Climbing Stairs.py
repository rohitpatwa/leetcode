# For each step, cost[i] += min(cost[i-1], cost[i-2]); return cost[-1]


def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return cost[-1]
        
#         cost.append(0)
#         n = len(cost)
#         if n==0:
#             return 0
#         elif n==1:
#             return cost[0]
#         else:
#             self.dp = [None]*n
#             self.dp[:2] = [cost[0], cost[1]]
#         self.helper(cost, n-1)
#         return self.dp[-1]
        
        
#     def helper(self, cost, i):
#         if self.dp[i] is not None:
#             return self.dp[i]
        
#         self.dp[i] = cost[i] + min(self.helper(cost, i-1), self.helper(cost, i-2))
#         return self.dp[i]