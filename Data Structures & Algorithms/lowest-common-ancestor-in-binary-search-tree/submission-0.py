# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # paralel binary search while pointer is common

        i, j = root, root
        while True:
            ti, tj = i, j #temporary
            if p.val < i.val:
                ti = i.left
            elif p.val > i.val:
                ti = i.right
            else:
                break
            
            if q.val < j.val:
                tj = j.left
            elif q.val > i.val:
                tj = j.right
            else:
                break

            if ti != tj:
                break
            else:
                i, j = ti, tj

        return i