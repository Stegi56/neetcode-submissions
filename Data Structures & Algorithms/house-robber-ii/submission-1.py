class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return sum(nums)

        def bestPath(skip):
            robL, robR = 0, 0
            for i , n in enumerate(nums):
                if i != skip:
                    temp = max(n + robL, robR)
                    robL = robR
                    robR = temp
            return robR

        return max(bestPath(0), bestPath(len(nums) - 1))