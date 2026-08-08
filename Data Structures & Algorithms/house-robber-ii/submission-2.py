class Solution:
    def rob(self, nums: List[int]) -> int:
        def bestPath(skip):
            robL, robR = 0, 0
            for i , n in enumerate(nums):
                if i != skip:
                    temp = max(n + robL, robR)
                    robL = robR
                    robR = temp
            return robR

        return max(nums[0], bestPath(0), bestPath(len(nums) - 1))