class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 1, 1

        for i in range(n):
            previous, current = current, current + previous

        return previous