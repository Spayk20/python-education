class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        self.length += 1

    def pop(self):
        if self.length > 0:
            res = self.head.data
            self.head = self.head.next
            self.length -= 1
            return res
        raise IndexError("No elements in stack")

    def __len__(self):
        return self.length


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print((stk.pop()))
print((stk.pop()))

a = 'aaa'
print(hash(a))
