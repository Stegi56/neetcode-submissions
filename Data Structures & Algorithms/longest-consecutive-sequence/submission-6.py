class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            counter = 0
            if (n - 1) not in nums:
                while (n + counter) in nums:
                    counter += 1
            longest = max(longest, counter)
        
        return longest