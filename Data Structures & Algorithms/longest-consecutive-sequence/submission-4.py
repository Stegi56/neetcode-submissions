class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        prevNum = nums[0]
        counter = 1
        greatest = 1

        for n in nums:
            if n == (prevNum + 1):
                counter += 1
                greatest = max(greatest, counter)
            elif n == prevNum:
                pass
            else:
                counter = 1
            prevNum = n
        
        return greatest