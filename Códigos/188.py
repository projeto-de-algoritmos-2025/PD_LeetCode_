class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
          
        # Se k >= n//2 = transações ilimitadas
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit

        # DP: dp[t][d] = lucro máximo com t transações até dia d
        dp = [[0] * n for _ in range(k + 1)]
        for t in range(1, k + 1):
            max_diff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d-1], prices[d] + max_diff)
                max_diff = max(max_diff, dp[t-1][d] - prices[d])
        return dp[k][n-1]
