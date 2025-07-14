from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        # 1. Juntar os jobs e ordenar por endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # DP e pontos de tempo para busca binária
        dp = [(0, 0)]  # (endTime, max_profit)
        
        for s, e, p in jobs:
            # 2. Busca binária:  # Extraímos os endTimes da tupla para busca binária
            i = bisect_right(dp, (s, float('inf'))) - 1
            curr_profit = dp[i][1] + p
            
            # 3. Atualiza dp se esse lucro for maior que o anterior
            if curr_profit > dp[-1][1]:
                dp.append((e, curr_profit))
        
        return dp[-1][1]
