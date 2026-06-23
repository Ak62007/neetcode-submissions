# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        else:
            loop_flag = False
            h_map = set()
            cur = head
            while cur is not None:
                if cur in h_map:
                    loop_flag = True
                    break
                else:
                    h_map.add(cur)
                cur = cur.next

            return loop_flag

