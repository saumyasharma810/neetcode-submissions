# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            temp = temp.next
            size+=1
        prev = None
        curr = head
        next_node = head.next
        pos = 1
        while pos != ((size - n) + 1):
            prev = curr
            curr = curr.next
            next_node = next_node.next
            pos += 1
        if curr == head:
            return head.next
        prev.next = next_node
        del curr
        return head
        

        

        