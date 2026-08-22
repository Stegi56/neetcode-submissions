class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robInRange(start, end):
            best, prev = 0, 0
            for i in range(start, end):
                num = nums[i]
                tmp = best
                best = max(best, prev + num)
                prev = tmp
            return best
        
        return max(
            robInRange(1, len(nums)),
            robInRange(0, len(nums) - 1)
        )
