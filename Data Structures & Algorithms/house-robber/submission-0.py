class Solution:
    def rob(self, nums: List[int]) -> int:
        robL, robR = 0, 0

        for n in nums:
            temp = max(n + robL, robR)
            robL = robR
            robR = temp
        
        return robR