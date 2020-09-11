class Singleton:
	_obj = None

	def __init__(self):
		raise RuntimeError('Call instance() method')

	@classmethod
	def instance(cls):
		if cls._obj is None:
			print('Creating instance of class')
			cls._obj = cls.__new__(cls)
		return cls._obj

# s1 = Singleton() #gives Runtime Error
obj1 = Singleton.instance()
print(obj1)
obj2 = Singleton.instance()
print(obj2)
if obj1 is obj2: print('both objects are same')
else: print('objects are not same')