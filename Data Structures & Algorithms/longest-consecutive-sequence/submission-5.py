class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for n in nums:
            it = n
            counter = 0
            if (n - 1) not in nums:
                while it in nums:
                    it += 1
                    counter += 1
            longest = max(longest, counter)
        
        return longest