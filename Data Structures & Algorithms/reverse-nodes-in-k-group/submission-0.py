# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_ll(head: ListNode) -> ListNode:
    prev_head = head
    tail = head.next
    head.next = None

    while tail:
        new_tail = tail.next
        tail.next = head
        head = tail
        tail = new_tail

    return head, prev_head

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # let's first get the length of the LinkedList
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        steps_to_take = n // k
        steps_taken = 0

        dummy = ListNode()
        d_cur = dummy
        
        while steps_taken != steps_to_take:
            cur = head
            step = 0
            while step != k-1:
                cur = cur.next
                step += 1

            prev_head = head
            head = cur.next
            cur.next = None

            r_head, r_prev_head = reverse_ll(prev_head)

            d_cur.next = r_head
            d_cur = r_prev_head

            steps_taken += 1

        d_cur.next = head

        return dummy.next