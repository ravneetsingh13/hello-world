import collections
lst = collections.deque(['A','B','C'])
lst.append('D')
print(lst)
lst.appendleft(1)
print(lst)
lst.insert(1,2)
print(lst)
lst.pop()
print(lst)
lst.popleft()
print(lst)
lst.remove('B')
print(lst)
lst.reverse()
print(lst)
print(lst.index('A'))
del lst[1]
print(lst)
lst.clear()
print(lst)