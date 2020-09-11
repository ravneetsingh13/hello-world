from LinkedList import LinkedList,Node

def reverseLL(node,prev):
	if node:
		next = node.next
		node.next = prev
		prev = node
		node = next
		reverseLL(node,prev)
	else:
		llist.head = prev

llist = LinkedList()
first = Node('a')
second = Node('b')
third = Node('c')
forth = Node('d')
fifth = Node('e')

llist.head = first
first.next = second
second.next = third
third.next = forth
forth.next = fifth

print("LL before recursion:",llist)
reverseLL(llist.head,None)
print("LL after recursion:",llist)