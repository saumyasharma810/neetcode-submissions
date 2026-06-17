# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        temp1, temp2 = l1, l2
        # print(temp1.val)
        curr = None
        carry = 0
        prev = None
        while temp1 and temp2:
            curr = ListNode((temp1.val + temp2.val + carry)% 10)
            if prev:
                prev.next = curr
            if not head:
                head = curr
            carry = (temp1.val + temp2.val + carry)//10
            prev = curr
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:
            curr = ListNode((temp1.val+carry)% 10)
            if prev:
                prev.next = curr
            if not head:
                head = curr
            carry = (temp1.val+carry)//10
            prev = curr
            temp1 = temp1.next
        
        while temp2:
            curr = ListNode((temp2.val + carry)% 10)
            if prev:
                prev.next = curr
            if not head:
                head = curr
            carry = (temp2.val + carry)//10
            prev = curr
            temp2 = temp2.next

        if carry:
            prev.next = ListNode(1)


        return head



        