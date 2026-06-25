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
        cur = head
        store = {}
        new_head = Node(0)
        new_cur = new_head
        while cur is not None:
            new_node = Node(cur.val)
            store[cur] = new_node
            new_cur.next = new_node
            cur = cur.next
            new_cur = new_cur.next

        new_copy = new_head.next
        new_cur = new_copy
        cur = head

        while cur is not None:
            if cur.random:
                new_cur.random = store[cur.random]
            else:
                new_cur.random = None
            new_cur = new_cur.next
            cur = cur.next

        return new_copy
