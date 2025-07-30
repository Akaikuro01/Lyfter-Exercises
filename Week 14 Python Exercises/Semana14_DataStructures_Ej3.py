class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.insert_recursive(self.root, value)

    def insert_recursive(self, current, value):
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)

    def print_tree(self):
        self.print_inorder(self.root)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.data)
            self.print_inorder(node.right)


root_node = Node(8)
tree = BinaryTree(root_node)

tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)

tree.print_tree()
