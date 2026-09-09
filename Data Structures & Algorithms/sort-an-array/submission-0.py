class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        sorting = True
        while sorting:
            sorting = False
            for i in range(length):
                j = i + 1
                if j < length:
                    if nums[i] > nums[j]:
                        sorting = True
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
        
        return nums