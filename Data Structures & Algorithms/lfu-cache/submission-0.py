class ListNode:
    def __init__(self, val: int, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val: int):
        node = ListNode(val, self.right.prev, self.right)
        node.prev.next = node
        self.right.prev = node
        self.map[val] = node
    
    def pop(self, val: int):
        if val in self.map:
            node = self.map[val]
            prev, next = node.prev, node.next
            prev.next, next.prev = next, prev
            self.map.pop(val)

    def popLeft(self):
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val: int):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_cnt = 0
        self.val_map = {}
        self.cnt_map = defaultdict(int)
        self.list_map = defaultdict(DoublyLinkedList)

    def counter(self, key:int):
        cnt = self.cnt_map[key]
        self.cnt_map[key] += 1
        self.list_map[cnt].pop(key)
        self.list_map[cnt + 1].pushRight(key)

        if cnt == self.min_cnt and self.list_map[cnt].length() == 0:
            self.min_cnt += 1

    def get(self, key: int) -> int:
        if key not in self.val_map:
            return -1
        else:
            self.counter(key)
            return self.val_map[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.val_map and len(self.val_map) == self.cap:
            res = self.list_map[self.min_cnt].popLeft()
            self.val_map.pop(res)
            self.cnt_map.pop(res)

        self.val_map[key] = value
        self.counter(key)
        self.min_cnt = min(self.min_cnt, self.cnt_map[key])

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)