# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        l = 1
        new_head = None
        prev = None
        prev_reversal = None
        while curr:
            ref = curr
            # check do we need to reverse
            check_curr = curr
            check_l = l
            while check_curr and check_l < k:
                check_curr = check_curr.next
                check_l += 1
            if not check_curr or check_l < k:
                break
            while curr and l < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                l+=1
            if l < k or not curr:
                break
            if not new_head:
                new_head = curr
            if prev_reversal:
                prev_reversal.next = curr
            next_node = curr.next
            curr.next = prev
            prev = None
            curr = next_node
            ref.next = next_node
            prev_reversal = ref
            l = 1
        if not new_head:
            new_head = head
        return new_head

        