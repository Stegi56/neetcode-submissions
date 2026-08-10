# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n: Optional[TreeNode], smallest: int, largest: int) -> bool:
            if n:
                if n.val > smallest and n.val < largest:
                    return dfs(n.left, smallest, n.val) and dfs(n.right, n.val, largest)
                else:
                    return False
            else:
                return True

        return dfs(root, float("-inf"), float("inf"))

    

