# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            dummy = ListNode()
            cur = dummy
            cur1 = l1
            cur2 = l2
            add_further = 0
            while cur1 or cur2:

                v1 = cur1.val if cur1 else 0
                v2 = cur2.val if cur2 else 0

                s = v1 + v2 + add_further

                add_further = s // 10

                cur.next = ListNode(s % 10)
                cur = cur.next

                if cur1:
                    cur1 = cur1.next

                if cur2:
                    cur2 = cur2.next
            if add_further == 1:
                cur.next = ListNode(1)

            return dummy.next
