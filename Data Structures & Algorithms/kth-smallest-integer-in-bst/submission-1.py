# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        counter = 1

        def dfs(n: Optional[TreeNode]) -> int:
            if n:
                dfs(n.left)
                stack.append(n.val)
                dfs(n.right)

        dfs(root)
        return stack[k - 1]
