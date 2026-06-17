"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        mapper = defaultdict(Node)
        curr = head
        prev = None
        while curr:
            mapper[curr] = Node(curr.val)
            if prev:
                prev.next = curr
                mapper[prev].next = mapper[curr]
            prev = curr
            curr = curr.next
        curr = head
        while curr:
            mapper[curr].random = mapper[curr.random] if curr.random is not None else None
            curr = curr.next
        return mapper[head]
            