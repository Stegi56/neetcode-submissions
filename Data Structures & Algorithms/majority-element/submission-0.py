class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        target = int(len(nums) / 2)

        count = 0
        num = nums[0]
        for n in nums:
            if n == num:
                count +=1
                if count > target:
                    return num
            else:
                count = 1
                num = n