# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        a = head
        if head.next == None:
            return head

        b = head.next
        if head.next.next == None:
            b = head.next
            head.next = None
            b.next = head
            return b

        c = head.next.next
        a.next = None

        def reverseL(x, y, z):
            y.next = x
            if z != None:
                return reverseL(y, z, z.next)
            else:
                return y
        
        return reverseL(a, b, c)

        