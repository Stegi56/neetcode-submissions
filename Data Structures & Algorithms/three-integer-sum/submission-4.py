class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        prevI = float("inf")
        for i in range(len(nums)):
            if nums[i] == prevI:
                continue

            l, r = i + 1, len(nums) - 1
            prevL, prevR = float("-inf"), float("inf")
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if (total > 0) or (nums[r] == prevR):
                    r = r - 1
                elif (total < 0) or (nums[l] == prevL):
                    l = l + 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    prevI, prevL, prevR = nums[i], nums[l], nums[r]
            
        return res

        