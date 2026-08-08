from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(n, resCopy):
            for val in resCopy:
                vc = val.copy()
                vc.append(n)
                res.append(vc)

        for i in nums:
            if res != [[]]:
                resCopy = res.copy()
                dfs(i, resCopy)
            else:
                res = [[], [i]]
        
        return res

