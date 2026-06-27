class ListNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = ListNode(-1, -1)
        self.left.nxt, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.prev, node.nxt = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            del self.cache[lru.key]
            self.remove(lru)
