# https://leetcode.com/problems/lfu-cache/description/
""" 
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
"""
from collections import defaultdict


class Node:
    def __init__(self, key=0, val=0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val
        self.freq = 1


class DDL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def delete(self, node=None):
        if not node:
            # As it will be the first inserted node
            node = self.tail.prev

        if node == self.head:
            return

        # print('\n',node.key,node.val)

        # Delete the node
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None
        self.size -= 1
        return node.key

    def dis(self):
        temp = self.head.next
        while temp:
            print('v:', temp.val, 'k:', temp.key, 'f:', temp.freq, end='  ')
            temp = temp.next


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = dict()
        self.freqList = defaultdict(DDL)
        self.minFreq = 0

    def get(self, key: int) -> int:
        # print('\n get start')
        if key not in self.hashMap:
            return -1

        # After getting the key update its frequency
        node = self.hashMap[key]
        val = node.val
        freq = node.freq

        self.freqList[freq].delete(node)

        newNode = Node(key, val)
        newNode.freq = freq+1

        if self.minFreq == freq and len(self.freqList[freq]) == 0:
            self.minFreq += 1

        self.freqList[freq+1].insert(newNode)
        self.hashMap[key] = newNode

        # print('minFreq',self.minFreq)
        # print('\n GET',key)
        # print('len:',freq,len(self.freqList[freq]))
        # self.freqList[freq].dis()
        # print('\n len:',freq+1,len(self.freqList[freq+1]))
        # self.freqList[freq+1].dis()

        return val

    def put(self, key: int, value: int) -> None:
        # print('\n put start')

        # If key already in hashMap update it
        # print('puminFreq',self.minFreq)
        if key in self.hashMap:
            # print('in')
            node = self.hashMap[key]
            freq = node.freq

            self.freqList[freq].delete(node)

            newNode = Node(key, value)
            newNode.freq = freq+1

            if self.minFreq == freq and len(self.freqList[freq]) == 0:
                self.minFreq += 1

            self.freqList[freq+1].insert(newNode)
            self.hashMap[key] = newNode

        else:
            if self.capacity == len(self.hashMap):
                # Remove the LFU
                dkey = self.freqList[self.minFreq].delete()

                del self.hashMap[dkey]

            newNode = Node(key, value)

            self.hashMap[key] = newNode

            self.freqList[1].insert(newNode)

            self.minFreq = 1

        # print('\n PUT',key,value)
        # self.freqList[1].dis()


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
