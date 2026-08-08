class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in nums:
            if i not in myMap:
                myMap[i] = 1
            else:
                return True
        return False