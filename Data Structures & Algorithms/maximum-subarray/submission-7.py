class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best, cur = nums[0], nums[0]

        for i in range(1, len(nums)):
            best = max(best, nums[i], cur + nums[i])
            cur = max(cur + nums[i], nums[i])

        return best