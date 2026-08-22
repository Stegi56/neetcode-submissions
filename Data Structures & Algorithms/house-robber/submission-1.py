class Solution:
    def rob(self, nums: List[int]) -> int:
        best, prev = 0, 0

        for num in nums:
            tmp = best
            best = max(best, prev + num)
            prev = tmp

        return best