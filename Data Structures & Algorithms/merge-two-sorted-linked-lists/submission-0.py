# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        temp = None
        head = None
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    temp = list1
                    head = temp
                else:
                    temp.next = list1
                    temp = temp.next
                list1 = list1.next
            else:
                if not head:
                    temp = list2
                    head = temp
                else:
                    temp.next = list2
                    temp = temp.next
                list2 = list2.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return head
        
                


        
        