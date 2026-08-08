# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node, counter):
            nonlocal depth
            counter += 1
            depth = max(counter, depth)
            if node.right:
                dfs(node.right, counter)
            if node.left:
                dfs(node.left, counter)
        if root:
            dfs(root, 0)
        else:
            return 0
        return depth
