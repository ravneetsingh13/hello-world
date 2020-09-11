import array as arr
a = arr.array('i',[1,2,3,4,5])
b = arr.array(a.typecode, [i*i for i in a])
b.reverse()
for e in a:
	print(e,end=' ')
print('\n')
for e in b:
	print(e,end=' ')
