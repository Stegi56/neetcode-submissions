class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minimum, maximum = 1, 1
        for n in nums:
            tmp = maximum
            maximum = max(maximum * n, minimum * n, n)
            minimum = min(minimum * n, tmp * n, n)
            res = max(res, maximum)
        
        return res