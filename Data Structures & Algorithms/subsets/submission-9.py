from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]


        for n in nums:
            resCopy = res.copy()
            for val in resCopy:
                vc = val.copy()
                vc.append(n)
                res.append(vc)

        
        return res

