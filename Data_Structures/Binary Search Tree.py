class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.length = 0

    def lookup(self, data):

        last = self.head

        while last:
            if last.data < data:
                last = last.right
            elif last.data > data:
                last = last.left
            elif last.data == data:
                return last

    def insert(self, data):

        if self.head is None:
            self.head = Node(data=data)
            self.length += 1
            return

        last = self.head

        while True:
            if last.data > data:
                if last.left is None:
                    last.left = Node(data)
                    break
                last = last.left

            elif last.data < data:
                if last.right is None:
                    last.right = Node(data)
                    break
                else:
                    last = last.right
            else:
                break

    @staticmethod
    def _min_value(last):
        while last.left is not None:
            last = last.left
        return last

    def delete(self, data):
        # check case tree is empty
        if self.head is None:
            raise IndexError("Not find in tree")

        last = self.head

        self._delete(last, data)

    def _delete(self, last, data):
        # if value not found in tree
        # print(last)
        if last is None:
            raise ValueError("Not <binarytree.Node object>")

        if data < last.data:

            last.left = self._delete(last=last.left, data=data)

        elif data > last.data:

            last.right = self._delete(last=last.right, data=data)

        else:

            if last.left is None:
                last = last.right
                return last

            if last.right is None:
                last = last.left
                return last

            temp = self._min_value(last.right)

            last.data = temp.data
            last.right = self._delete(last.right, temp.data)

        return last

    def printTree(self):
        last = self.head

        def printer(last):
            if last.left:
                printer(last.left)
            print(last.data)
            if last.right:
                printer(last.right)
        printer(last)

    root = Node(12)

bts = BinarySearchTree()
bts.insert(12)
bts.insert(34)
bts.insert(10)
bts.insert(52)
bts.insert(2021)
bts.insert(25)
bts.insert(1999)
bts.insert(76)
bts.insert(90)
bts.insert(684)
bts.insert(40)
bts.insert(271)
bts.insert(27)
bts.insert(265)
bts.printTree()

print('\n')
bts.delete(10)
bts.printTree()

print('\n')
bts.delete(34)
bts.printTree()

print('\n')
bts.insert(98)
bts.printTree()


print(bts.lookup(27))