class Stack:
    def __init__(self, data=None):
        self.top = -1
        self.stack = []
        if data is not None:
            for e in data:
                self.top += 1
                self.stack.append(e)

    def __repr__(self):
        return repr(self.stack)

    def push(self, value):
        self.top += 1
        self.stack.append(value)

    def pop(self):
        if(self.isEmpty()):
            return 'Stack is Empty'
        else:
            e = self.peek()
            del self.stack[self.top]
            self.top -= 1
            return e

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1
        # return len(stack) == 0 ...both return methods are correct


s = Stack()
print(s.isEmpty())
s.push(1)
print(s.isEmpty())
s.push(2)
print(s.peek())
s.push(3)
print(s)
print(s.pop())
print(s)

lst = ['a', 'b', 'c', 'd', 'e']
so = Stack(lst)
print(so)
print(so.size())
print(so.pop())
print(so.pop())
print(so.pop())
print(so.pop())
print(so.pop())
print(so)
print(so.pop())
so.push('j')
so.push('k')
so.push('i')
print(so)
