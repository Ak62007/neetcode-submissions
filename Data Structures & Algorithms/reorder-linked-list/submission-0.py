# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        nodes_with_idx = []
        while cur is not None:
            nodes_with_idx.append(cur)
            cur = cur.next

        if len(nodes_with_idx) <= 2:
            return
        else:
            head.next = nodes_with_idx[-1]
            cur = head.next
            i, j = 1, len(nodes_with_idx) - 2
            while i <= j:
                if i != j:
                    nodes_with_idx[i].next = None
                    cur.next = nodes_with_idx[i]
                    cur = cur.next
                    nodes_with_idx[j].next = None
                    cur.next = nodes_with_idx[j]
                    cur = cur.next
                    i += 1
                    j -= 1
                else:
                    nodes_with_idx[i].next = None
                    cur.next = nodes_with_idx[i]
                    break

            return