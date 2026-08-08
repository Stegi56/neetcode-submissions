# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        newStack = deque()
        res = []
        buildRes = []
        while stack or newStack or buildRes:
            if stack:
                node = stack.popleft()
                buildRes.append(node.val)
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            else: #reset and start next layer
                res.append(buildRes)
                buildRes = []
                stack = newStack
                newStack = deque()
        
        return res