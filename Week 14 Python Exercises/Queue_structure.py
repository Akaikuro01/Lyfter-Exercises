class Node:
	data: str

	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head


class Queue(LinkedList):
	def enqueue(self, new_node):
		current_node = self.head
		next_node = current_node.next
		while (next_node is not None):
			current_node = next_node
			next_node = current_node.next

		current_node.next = new_node

	def dequeue(self):
		self.head = self.head.next
	

	def print_structure(self):
		current_node = self.head					
		print(current_node.data)
		while(current_node.next is not None):
			current_node = current_node.next
			print(current_node.data)


first_node = Node("first")
my_queue = Queue(first_node)
# my_queue.print_structure()

second_node = Node("second")
my_queue.enqueue(second_node)

third_node = Node("third")
my_queue.enqueue(third_node)

forth = Node("forth")
my_queue.enqueue(forth)

my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()



