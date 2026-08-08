class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float("-inf")
        for i in range(len(nums)):
            tot = 0
            for j in range(i,len(nums)):
                tot += nums[j]
                if tot > max:
                    max = tot
        
        return max