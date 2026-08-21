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

        def mergeTwoLists(l, r):
            res = dummy = ListNode()
            while l and r:
                if l.val <= r.val:
                    res.next = l
                    l = l.next
                else:
                    res.next = r
                    r = r.next
                res = res.next
            
            if l and not r:
                res.next = l
            else:
                res.next = r

            return dummy.next

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l = lists[i]
                if i + 1 >= len(lists):
                    mergedLists.append(l)
                else:
                    r = lists[i + 1]
                    mergedLists.append(mergeTwoLists(l, r))
            lists = mergedLists

        return lists[0]
