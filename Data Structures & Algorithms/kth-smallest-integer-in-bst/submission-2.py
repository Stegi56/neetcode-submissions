# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        counter = k

        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal counter, res
            if n:
                dfs(n.left)
                if counter == 0:
                    return
                counter -=1
                if counter == 0:
                    res = n.val
                    return
                dfs(n.right)

        dfs(root)
        return res
