# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==1:
            return None
        k = 0
        sorted_list = []
        for x in lists:
            if x:
                sorted_list.append((x.val, k, x))
                k+=1
        heapq.heapify(sorted_list)
        head = None
        curr = None
        prev = None
        while sorted_list:
            curr = heapq.heappop(sorted_list)
            if not head:
                head = curr[2]            
            if curr[2].next:
                heapq.heappush(sorted_list,(curr[2].next.val, k, curr[2].next))
                k+=1
            if prev:
                prev.next = curr[2]
            prev = curr[2]
        return head

            
            


        
        