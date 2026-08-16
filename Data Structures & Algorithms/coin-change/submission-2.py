class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(lambda: float("inf"))
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                combo = i - coin
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[combo] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1