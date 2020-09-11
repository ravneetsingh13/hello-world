from LinkedList import LinkedList,Node

def printLL(node):
	if node:
		print(node.data,end=' ')
		printLL(node.next)

def printReverseLL(node):
	if node:
		printReverseLL(node.next)
		print(node.data,end=' ')



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

print("Printing with loop:",llist,sep='\n')
print("Printing using recursion:")
printLL(llist.head)
print("Printing reverse LL using recursion:")
printReverseLL(llist.head)