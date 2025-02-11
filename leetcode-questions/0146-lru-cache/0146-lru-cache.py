class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linkedList = {}
        self.head = self.tail = Node(0)
        
    def get(self, key: int) -> int:
        if key in self.linkedList:
            value, node = self.linkedList[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            
                self.tail.next = Node(key, self.tail, None)
                self.tail = self.tail.next
                self.linkedList[key] = [value, self.tail]
            
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        curr = Node(key, self.tail, None)
        self.tail.next = curr
        self.tail = self.tail.next
        if key in self.linkedList:
            val, node = self.linkedList[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.linkedList[key]
        
        self.linkedList[key] = [value, curr]
        if len(self.linkedList) > self.capacity:
            lru = self.head.next

            lru.next.prev = self.head
            self.head.next = lru.next

            del self.linkedList[lru.val]
        