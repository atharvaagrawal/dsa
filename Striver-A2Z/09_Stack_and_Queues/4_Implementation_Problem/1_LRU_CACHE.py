# https://leetcode.com/problems/lru-cache/description/

""" 
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""


class Node:

    def __init__(self, val=0, key=0):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class DDL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, node):
        return node.val

    def insert(self, key, val):
        temp = self.head

        newNode = Node(val, key)

        newNode.next = temp.next
        newNode.prev = temp

        temp.next.prev = newNode
        temp.next = newNode

        return newNode

    def delete(self, node):
        temp = node.prev
        temp2 = node.next

        temp.next = temp2
        temp2.prev = temp

        node.next = None
        node.prev = None
        del node

    def deleteLRU(self):
        temp = self.tail

        key = temp.prev.key
        temp.prev.prev.next = temp
        temp.prev = temp.prev.prev
        return key

    def dis(self):
        temp = self.head
        temp = temp.next

        while temp.next != None:
            print('k:', temp.key, 'v:', temp.val, end=' ')
            temp = temp.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict()
        self.ddl = DDL()

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        val = self.ddl.get(self.hashMap[key])

        self.ddl.delete(self.hashMap[key])
        self.hashMap[key] = self.ddl.insert(key, val)

        # print('get:',key,val)
        # print(self.ddl.dis())
        return val

    def put(self, key: int, value: int) -> None:

        # If key already exist
        if key in self.hashMap:
            # Delete it
            self.ddl.delete(self.hashMap[key])

        elif self.capacity == len(self.hashMap):
            # Now time to remove
            dkey = self.ddl.deleteLRU()
            del self.hashMap[dkey]

        self.hashMap[key] = self.ddl.insert(key, value)

        # print('put')
        # print(self.hashMap)
        # print(self.ddl.dis())

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
