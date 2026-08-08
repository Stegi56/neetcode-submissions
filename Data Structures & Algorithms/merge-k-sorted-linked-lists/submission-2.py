# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if not lists:
        #     return None
        
        # tail = head = ListNode(0, None)

        # while any(item is not None for item in lists):
        #     lowestIndex, lowestValue = 0, float("inf")
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if lists[i].val < lowestValue:
        #             lowestValue = lists[i].val
        #             lowestIndex = i
            
        #     copy = ListNode(lowestValue, None)
        #     if not lists[lowestIndex]:
        #         break
        #     else:
        #         lists[lowestIndex] = lists[lowestIndex].next #remove
        #         tail.next = copy
        #         tail = tail.next

        # return head.next

        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []
            for l in range(0, len(lists), 2):
                a = lists[l]
                b = lists[l+1] if ((l + 1) < (len(lists))) else None
                mergedLists.append(self.mergeLists(a,b))
            lists = mergedLists

        return lists[0]

    def mergeLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode(0, None)

        while a and b:
            if a.val < b.val:
                tmp = a
                a = a.next
            else:
                tmp = b
                b = b.next
            tail.next = tmp
            tail = tail.next

        tail.next = a or b
        
        return head.next

