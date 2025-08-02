class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head


	def print_structure(self):
		current_node = self.head					
		print(current_node.data)
		while(current_node.next is not None):
			current_node = current_node.next
			print(current_node.data)


fourth_node = Node("Soy el cuarto nodo")
third_node = Node("Soy el tercer nodo", fourth_node)
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()