
class Queue(object):
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0,item)
	
	def dequeue(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)

q = Queue()

print(q.isEmpty())
q.enqueue("hello")
q.enqueue("world")
print(q.isEmpty())
print(q.size())
print(q.dequeue())
