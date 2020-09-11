class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)


class DoublyLL:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            self.tail = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
                node.prev = self.tail
                self.tail = node

    def __repr__(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        return "None"

    def printReverse(self):
        node = self.tail
        while node:
            print(node.data, end=" <-> ")
            node = node.prev
        print(None)


dll = DoublyLL(['a', 'b', 'c', 'd'])
print(dll)
DoublyLL.printReverse(dll)
