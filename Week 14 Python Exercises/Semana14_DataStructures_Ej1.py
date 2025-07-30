class Node:
	data: str

	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head


class Stack(LinkedList):
	def push(self, new_node):
		new_node.next = self.head
		self.head = new_node


	def pop(self):
		self.head = self.head.next


	def print_structure(self):
		current_node = self.head					
		print(current_node.data)
		while(current_node.next is not None):
			current_node = current_node.next
			print(current_node.data)




first_node = Node("first")
my_stack = Stack(first_node)

second_node = Node("second")
my_stack.push(second_node)

third_node = Node("third")
my_stack.push(third_node)

forth = Node("forth")
my_stack.push(forth)

my_stack.print_structure()

print("pop")

my_stack.pop()
my_stack.print_structure()

print("pop")

my_stack.pop()
my_stack.print_structure()

print("pop")

my_stack.pop()
my_stack.print_structure()