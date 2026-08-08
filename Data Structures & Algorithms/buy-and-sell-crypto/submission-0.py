class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i, ip in enumerate(prices):
            for j in range(i, len(prices)):
                if (prices[j] - ip) > best:
                    best = prices[j] - ip
        return best

