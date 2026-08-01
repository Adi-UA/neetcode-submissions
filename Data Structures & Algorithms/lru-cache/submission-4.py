class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.next=self.previous=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        
        # initialize and link left/right
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.previous=self.right,self.left

    def remove(self, node):
        node.previous.next=node.next
        node.next.previous=node.previous

    def insert(self, node):
        nxt,prev=self.right,self.right.previous
        node.next,node.previous=nxt,prev

        prev.next=node
        nxt.previous=node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        # if exceed capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            