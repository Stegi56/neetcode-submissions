class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        top = l

        while top > 0:
            for i in range(0, top - 1):
                if nums[i] > nums[i + 1]:
                    tmp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = tmp
            top -= 1
