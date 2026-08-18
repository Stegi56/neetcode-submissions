class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)

        def dfs(i) -> int:
            if i in dp:
                return dp[i]

            res = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))

            dp[i] = res
            return res

        for i in range(len(nums), -1, -1):
            dfs(i)

        return max(dp.values())