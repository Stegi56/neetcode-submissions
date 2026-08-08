# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes = set()

        curNode = head
        while curNode:
            seenNodes.add(curNode)
            if curNode.next:
                if curNode.next in seenNodes:
                    return True
                else:
                    curNode = curNode.next
            else:
                break

        return False