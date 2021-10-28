class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Get methods
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # Set methods
    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return

        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def lookup(self, data):
        cur_node = self.head
        res = None
        index = 0

        if cur_node:
            while cur_node:
                if data != cur_node.data:
                    cur_node = cur_node.next
                elif data == cur_node.data:
                    res = index
                    break
                index += 1
        if res is None:
            res = None
        return res

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.append(data)
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def delete(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.remove_data()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += str(cur_node.get_data()) + "--"
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def remove_data(self):
        cur_node = self.head
        self.head = cur_node.get_next()


llist = LinkedList()
llist.append(2)
llist.append(4)
llist.append(8)
llist.append(16)
llist.prepend(32)
llist.show()
llist.length()
llist.insert(2, 999)
print(llist.lookup(2))
llist.show()
llist.delete(2)
llist.show()
