class MyHashSet:

    def __init__(self):
        self.main_set = []

    def add(self, key: int) -> None:
        for num in self.main_set:
            if num == key:
                return
        self.main_set.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.main_set)):
            if self.main_set[i] == key:
                self.main_set.pop(i)
                return
        return

    def contains(self, key: int) -> bool:
        for num in self.main_set:
            if num == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)