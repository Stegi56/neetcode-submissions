# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preValInIndex = {}

        for i, n in enumerate(inorder):
            preValInIndex[n] = i

        def dfs(pre_start, pre_end, in_start, in_end):
            nonlocal preValInIndex
            if pre_start > pre_end:
                return None

            res = TreeNode(preorder[pre_start])
            mid = preValInIndex[preorder[pre_start]]
            left_size = mid - in_start
            #res.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            #res.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
            res.left = dfs(pre_start + 1, pre_start + left_size, in_start, mid)
            res.right = dfs(pre_start + left_size + 1, pre_end, mid + 1, in_end)

            return res

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)