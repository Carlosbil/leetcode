from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        return the max profit from buying and selling stocks across a period of time, taking the actual price and the best price in the future
        """
        lower = prices[0]
        best = 0
        if len(prices) > 2:
            for i in range(1, len(prices)):
                lower = min(lower, prices[i])
                diff = prices[i] - lower
                best = max(best, diff)                
        return best
 