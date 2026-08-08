# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        rmIndex = length - n
        if rmIndex == 0:
            return head.next
        
        cur = head
        for i in range(length - 1):
            if (i + 1) == rmIndex:
                cur.next = cur.next.next
                return head
            cur = cur.next

        return head