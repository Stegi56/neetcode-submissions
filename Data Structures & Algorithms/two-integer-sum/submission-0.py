class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(nums):
            if target - n in myMap.keys():
                return [myMap[target -n], i]
            else:
                myMap[n] = i