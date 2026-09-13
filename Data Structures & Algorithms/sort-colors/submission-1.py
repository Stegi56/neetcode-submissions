class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros, ones, twos = 0, 0, 0
        for i in range(len(nums)):
            match nums[i]:
                case 0:
                    zeros += 1
                case 1:
                    ones += 1
                case 2:
                    twos += 1
                case _:
                    None
        
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            elif twos > 0:
                nums[i] = 2
                twos -= 1