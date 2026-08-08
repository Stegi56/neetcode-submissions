class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, cur = nums[0], 0

        for n in nums:
            if cur < 0:
                cur = n
            else:
                cur += n

            best = max(best, cur)
        
        return best