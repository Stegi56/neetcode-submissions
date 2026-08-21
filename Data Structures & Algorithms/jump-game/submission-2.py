class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # dp = {}
        # def dfs(pos: int) -> bool:
        #     if pos in dp:
        #         return dp[pos]

        #     if pos >= len(nums) - 1:
        #         return True

        #     maxJump = nums[pos]
        #     if maxJump == 0:
        #         dp[pos] = False
        #         return False

        #     res = False
        #     for jump in range(maxJump, 0, -1):
        #         res = res or dfs(pos + jump)
        #     dp[pos] = res
        #     return res

        # return dfs(0)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        
        return goal == 0