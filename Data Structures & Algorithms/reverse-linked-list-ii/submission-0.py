# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head
        elif left == right:
            return head
        cur = head
        i = 1
        imd = None
        while cur:
            if i == (left-1) and left != 1:
                imd = cur
            while left <= i <= right:
                if i == left:
                    r_head = cur
                    new_head = cur.next
                    cur.next = None
                    tail = cur
                    cur = new_head
                else:
                    new_head = cur.next
                    cur.next = tail
                    tail = cur
                    cur = new_head
                i += 1
            if i > right:
                if cur:
                    r_head.next = cur
                else:
                    r_head.next = None
                if imd:
                    imd.next = tail
                else:
                    head = tail
                break

            i += 1
            cur = cur.next

        return head            