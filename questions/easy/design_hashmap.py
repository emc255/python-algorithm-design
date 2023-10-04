"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.

"""


class MyHashMap:

    def __init__(self):
        self.pair = None

    def put(self, key: int, value: int) -> None:
        new_pair = Pair(key, value)
        if self.pair is None:
            self.pair = new_pair
        else:
            prev = None
            current = self.pair
            while current:
                if current.key == key:
                    current.value = value
                    return
                
                prev, current = current, current.next

            prev.next = new_pair

    def get(self, key: int) -> int:
        current = self.pair
        while current:
            if current.key == key:
                return current.value
            current = current.next

        return -1

    def remove(self, key: int) -> None:
        if self.pair is None:
            return

        if self.pair.key == key:
            self.pair = self.pair.next

        prev = None
        current = self.pair

        while current:
            if current.key == key:
                prev.next = current.next

            prev = current
            current = current.next


class Pair:
    def __init__(self, key: int, value: int, next_pair: 'Pair' = None):
        self.key = key
        self.value = value
        self.next = next_pair


a = MyHashMap()
a.put(1, 1)
a.put(2, 2)
print(a.get(1))
print(a.get(3))
a.put(2, 1)
print(a.get(2))
v = a.pair
while v:
    print(f'key = {v.key} || value = {v.value}')
    v = v.next
