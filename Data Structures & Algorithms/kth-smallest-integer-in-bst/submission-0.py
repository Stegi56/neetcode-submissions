# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []

        def dfs(n: Optional[TreeNode]) -> None:
            if n:
                dfs(n.left)
                dfs(n.right)
                heapq.heappush(minHeap, n.val)

        dfs(root)
    
        res = -1
        for i in range(k):
            res = heapq.heappop(minHeap)

        return res