class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

def invert_binary_tree(root):
    if root is None:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Invert the left and right subtrees recursively
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root

def print_binary_tree(root):
    print_tree(root, 0)

def print_tree(node, level):
    if node is None:
        return
    if node == node.data:
        # Print the root node
        print(str(node.data))
    # Print sunsequent nodes
    print_tree(node.right, level + 1)
    print('  ' * level + str(node.data))
    print_tree(node.left, level + 1)


numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree.delete(20)
print("After deleting 20 ",numbers_tree.in_order_traversal())
print(f'This is the minimum value: {numbers_tree.find_max()}, this is the maximum value {numbers_tree.find_min()}')
inverted = invert_binary_tree(numbers_tree)
print(inverted.in_order_traversal())
print_binary_tree(inverted)




