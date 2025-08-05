class Node:
	data: int

	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class LinkedList:
	head: Node

	def __init__(self, head, length=1):
		self.head = head
		self.length = length


class Queue(LinkedList):
	def enqueue(self, new_node):
		current_node = self.head
		next_node = current_node.next
		while (next_node is not None):
			current_node = next_node
			next_node = current_node.next

		current_node.next = new_node
		self.len_queue(True)

	def dequeue(self):
		self.head = self.head.next
		self.len_queue(False)
	
	def print_structure(self):
		current_node = self.head	
		print(f"Amount of elements in the queue: {self.length}")				
		print(current_node.data)
		while(current_node.next is not None):
			current_node = current_node.next
			print(current_node.data)
	
	def len_queue(self, add):		
		if(add == True):
			self.length += 1
		else:
			self.length -= 1

	def bubble_sort(self):
		current_node = self.head
		outer_counter = 1
		counter = 1
		while(outer_counter < self.length):			
			swapped = False
			while(counter < self.length):
				current_node_element = current_node.data
				next_node_element = current_node.next.data
				if (current_node_element > next_node_element):
					current_node.data = next_node_element
					current_node.next.data = current_node_element
					swapped = True		
				current_node = current_node.next
				counter += 1
			if (swapped == False):
				break
			else:				
				counter = 1 + outer_counter
				outer_counter += 1
				current_node = self.head



first_node = Node(5)
my_queue = Queue(first_node)
# my_queue.print_structure()

second_node = Node(1)
my_queue.enqueue(second_node)

third_node = Node(4)
my_queue.enqueue(third_node)

forth = Node(2)
my_queue.enqueue(forth)

my_queue.print_structure()

my_queue.bubble_sort()

my_queue.print_structure()
