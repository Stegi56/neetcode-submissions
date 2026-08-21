# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle pointer
        #reverse from the middle
        #shuffle vals in

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        l, r = head, prev
        while r:
            tmpL, tmpR = l.next, r.next
            l.next, r.next = r, tmpL
            l, r = tmpL, tmpR
        
