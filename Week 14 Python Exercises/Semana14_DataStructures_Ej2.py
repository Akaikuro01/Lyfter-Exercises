class Node:
	data: str

	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev


class LinkedList:
	head: Node
	tail: Node

	def __init__(self, head, tail=None):
		self.head = head
		self.tail = tail


class Deque(LinkedList):
	def push_left(self, new_node):
		self.head.prev = new_node
		new_node.next = self.head
		self.head = new_node
	
	def push_right(self, new_node):
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node
		


	def pop_left(self):
		self.head = self.head.next
		self.head.prev = None
	

	def pop_right(self):
		self.tail = self.tail.prev
		self.tail.next = None


	def print_structure(self):
		current_node = self.head					
		print(current_node.data)
		while(current_node.next is not None):
			current_node = current_node.next
			print(current_node.data)



first_node = Node("First")
my_deque = Deque(first_node, first_node)

second_node = Node("Second")
my_deque.push_right(second_node)

third_node = Node("third")
my_deque.push_right(third_node)

forth_node = Node("forth")
my_deque.push_right(forth_node)

my_deque.print_structure()

fifth_node = Node("fifth")
my_deque.push_left(fifth_node)

sixth_node = Node("sixth")
my_deque.push_left(sixth_node)

print("-----------------------")
my_deque.print_structure()

my_deque.pop_left()
print("--Popped left--")
my_deque.print_structure()
print("-----------------------")

my_deque.pop_left()
print("--Popped left--")
my_deque.print_structure()
print("-----------------------")

my_deque.pop_right()
print("--Popped right--")
my_deque.print_structure()
print("-----------------------")

my_deque.pop_right()
print("--Popped right--")
my_deque.print_structure()
print("-----------------------")

