class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self, nodes=None):  # l2 = LinkedList(['a','b','c'])
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node  # head variable has address of first node 'a' head -> 'a'
            for elem in nodes:  # b, c
                node.next = Node(elem)  # head -> a -> b -> c -> None
                node = node.next

    def __repr__(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        return 'None'

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # getter method
    def getList(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        return(nodes)

    # prepend
    def prepend(self, data):
        self.head = Node(data, next=self.head)

    # append
    def append(self, data):
        node = self.head
        if node is None:
            self.head = Node(data)
        else:
            while node.next:
                node = node.next
            node.next = Node(data)

    # insert
    def insert(self, data, n):
        if n == 1:
            self.head = Node(data, next=self.head)
        elif self.length() < n - 1 or n <= 0:
            raise Exception("Invalid Position")
        else:
            node = self.head
            i = 1
            while i < n - 1:
                node = node.next
                i += 1
            new_node = Node(data, next=node.next)
            node.next = new_node

    # length
    def length(self):
        if self.head is None:
            return 0
        else:
            node = self.head
            count = 1
            while node.next:
                node = node.next
                count += 1
        return count

    # find
    def find(self, key):
        node = self.head
        while node and node.data != key:
            node = node.next
        return node

    # remove
    def remove(self, key):
        node = self.head
        prev = None
        while node and node.data != key:
            prev = node
            node = node.next
        if prev is None:
            self.head = node.next
        elif node:
            prev.next = node.next
            node.next = None

    # reverse
    def reverse(self):
        node = self.head  # current points to first node
        prev_node = None  # prev points to None
        next_node = None  # next points to None
        while node:
            next_node = node.next  # move next one step ahead
            node.next = prev_node  # reverse the link
            prev_node = node  # move prev one step ahead
            node = next_node  # move current one step ahead to iterate further
        # assign prev to head pointer(as prev contains the current node-
        self.head = prev_node
        # which is last node of the list)


if __name__ == '__main__':
    # Creating Empty LinkedList
    l1 = LinkedList()
    print(l1)

    # inserting element at 1st position in empty linked list
    l1.insert(8, 1)
    print(l1)

    # #assign values to Nodes
    # first = Node(65)
    # second = Node(66)
    # third = Node(67)
    # forth = Node(68)
    # fifth = Node(69)

    # #Link Nodes
    # l1.head = first
    # first.next = second
    # second.next = third
    # third.next = forth
    # forth.next = fifth

    # calling prepend
    l1.prepend(64)
    print(l1)

    # calling append
    l1.append(70)
    print(l1)

    # calling insert with n position
    l1.insert(13, 2)

    # calling find
    print('found:', l1.find(1))

    # Calling __repr__ method on trying to print LinkedList object
    print(l1)

    # calling length
    print(l1.length())

    # getting LinkedList in form of List
    lst = l1.getList()
    print(lst)

    # Calling __iter__ method by doing iteration over LinkedList object
    for node in l1:
        print(node)

    # Calling remove
    l1.remove(13)
    print(l1)

    # Calling reverse
    l1.reverse()
    print(l1)

    # Creating LinkedList with data
    l2 = LinkedList(['a', 'b', 'c'])
    print(l2)
