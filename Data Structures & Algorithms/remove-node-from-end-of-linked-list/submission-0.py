# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next

        if length == 0:
            return None
        elif (length == 1) and (n == 1):
            return None
        else:
            if length == n:
                return head.next
            idx = length - n - 1
            i = 0
            cur = head
            while i != idx:
                i += 1
                cur = cur.next

            imd = cur.next.next
            cur.next = imd

            return head