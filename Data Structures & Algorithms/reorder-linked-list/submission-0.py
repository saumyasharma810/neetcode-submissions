# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left, right = head, head
        while right and right.next:
            left = left.next
            right = right.next.next
        curr = left
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        left, right = head, prev
        left_next = left.next
        right_next = right.next
        while left_next and right_next:
            print(left.val, right.val)
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next
            left_next = left.next
            right_next = right.next

        