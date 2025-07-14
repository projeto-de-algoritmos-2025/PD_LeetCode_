class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        max_k = 2

        dp = [[0] * n for _ in range(max_k + 1)]

        for k in range(1, max_k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[k][i] = max(dp[k][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[k-1][i] - prices[i])
        
        return dp[max_k][n-1]