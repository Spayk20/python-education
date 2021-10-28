class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_data = None


class Queue:

    def __init__(self):
        self.start = None
        self.head = None
        self.length = 0

    def enqueue(self, new_data):
        new_node = Node(data=new_data)

        # if self.head is empty, its will be start of list
        if self.head is None:
            self.start = new_node
            self.head = new_node
            self.length += 1
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        self.length += 1

    def peek(self):
        return self.head.data

    def dequeue(self):
        res = self.head.data
        self.head = self.head.next
        self.length -= 1
        return res

    def __len__(self):
        return self.length

que = Queue()
que.enqueue(1)
que.enqueue(2)
print(que.peek())
print(len(que))
print("dequeue", que.dequeue())
print("peek ", que.peek())
print("len: ", len(que))