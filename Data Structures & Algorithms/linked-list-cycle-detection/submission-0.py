# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes = []

        curNode = head
        while curNode:
            seenNodes.append(curNode)
            if curNode.next:
                if curNode.next in seenNodes:
                    return True
                else:
                    curNode = curNode.next
            else:
                break

        return False