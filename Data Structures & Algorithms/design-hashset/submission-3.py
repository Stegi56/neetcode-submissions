class Node:
    def __init__(self, val=None, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashmap = [None for i in range(0,10000)]

    def add(self, key: int) -> None:
        mapKey = key % 10000
        if self.hashmap[mapKey] == None:
            self.hashmap[mapKey] = Node(key)
        else:
            node = self.hashmap[mapKey]
            while node.next != None and node.val != key:
                node = node.next
            if node.val != key:
                node.next = Node(key)

    def remove(self, key: int) -> None:
        mapKey = key % 10000

        prev = dummy = Node()
        dummy.next = node = self.hashmap[mapKey]
        if not node:
            return
        while node.next != None and node.val != key:
            node = node.next
            prev = prev.next
        if node.val == key:
            prev.next = node.next
            self.hashmap[mapKey] = dummy.next

    def contains(self, key: int) -> bool:
        mapKey = key % 10000

        node = self.hashmap[mapKey]
        if not node:
            return False

        while node.next != None and node.val != key:
            node = node.next
        return node.val == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)