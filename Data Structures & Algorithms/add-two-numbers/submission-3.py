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
                if cur1 and cur2:
                    s = cur1.val + cur2.val
                    s += add_further
                    if s > 9:
                        add_further = 1
                        cur.next = ListNode(s % 10)
                    else:
                        add_further = 0
                        cur.next = ListNode(s)

                    cur = cur.next
                    cur1 = cur1.next
                    cur2 = cur2.next
                else:
                    if cur1:
                        s = cur1.val + add_further
                        if s > 9:
                            add_further = 1
                            cur.next = ListNode(s % 10)
                        else:
                            add_further = 0
                            cur.next = ListNode(s)
                        
                        cur = cur.next
                        cur1 = cur1.next
                    else:
                        s = cur2.val + add_further
                        if s > 9:
                            add_further = 1
                            cur.next = ListNode(s % 10)
                        else:
                            add_further = 0
                            cur.next = ListNode(s)

                        cur = cur.next
                        cur2 = cur2.next
                        

            # if cur1:
            #     if add_further != 0
            #     while 
            #     cur.next = cur1
            # else:
            #     cur.next = cur2

            if add_further == 1:
                cur.next = ListNode(1)

            return dummy.next
