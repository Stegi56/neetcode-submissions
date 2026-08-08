class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max, cur = nums[0], 0

        for n in nums:
            if cur < 0:
                cur = n
            else:
                cur += n

            if cur > max:
                max = cur
        
        return max