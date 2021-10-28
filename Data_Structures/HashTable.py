class Node:

    def __init__(self, data=None, next=None, hash=None):
        self.data = data
        self.next = next
        self.hash = hash


class HashTable:
    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, key):
        print(hash(key))
        key = hash(key)
        last = self.head
        res = None
        for i in range(self.length):
            if key != last.hash:
                last = last.next
            elif key == last.hash:
                res = last.data
                break
        if res is None:
            raise KeyError(f'{hash} not found')
        return res

    def insert(self, data, key):
        new_head = Node(data)
        new_head.next = self.head
        new_head.hash = hash(key)
        self.head = new_head
        self.length += 1

    def delete(self, index):
        if not isinstance(index, int):
            raise ValueError(f"index must be <class 'int'>, not {type(index)}")

        if index > self.length:
            # raise if elem bigger then list length
            raise IndexError("Index error, out of list")

        priv = self.head
        last = self.head
        for temp_index in range(self.length):
            print(f"priv: {priv.data}, last.data: {last.data}, temp_index: {temp_index}")

            if temp_index == index:
                priv.next = last.next
                self.length -= 1
                return
            priv = last
            last = last.next

    def __len__(self):
        return self.length


hsh = HashTable()
hsh.insert(1, 'a')
hsh.insert(2, 'b')
hsh.insert(3, 'c')
hsh.insert(4, 'd')
hsh.insert(5, 'e')
hsh.insert(6, 'f')
print(hsh.lookup('d'))
