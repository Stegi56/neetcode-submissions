class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lP = 0
        rP = len(nums) -1
        while lP <= rP:
            m = (lP + rP) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                lP = m  + 1
            else:
                rP = m - 1
        return -1

