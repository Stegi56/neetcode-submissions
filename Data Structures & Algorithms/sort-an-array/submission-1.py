class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        top = length
        sorting = True
        while sorting:
            sorting = False
            for i in range(top):
                j = i + 1
                if j < length:
                    if nums[i] > nums[j]:
                        sorting = True
                        top = j
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
        
        return nums