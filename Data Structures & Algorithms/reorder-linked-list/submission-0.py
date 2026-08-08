# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #set start pointer
        #set floor half pointer

        # reverse 2nd half

        #shuffle in 2nd reversed linked list

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1, l2 = head, prev
        cur = dummy = ListNode()
        alternator = "l"
        while l1 and l2:
            if alternator == "l":
                cur.next = l1
                l1 = l1.next
                alternator = "r"
            else:
                cur.next = l2
                l2 = l2.next
                alternator = "l"
            cur = cur.next

        cur.next = l1 or l2

        head.next = dummy.next.next

