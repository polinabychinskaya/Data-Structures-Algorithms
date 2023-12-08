class BinarySearchTreeNode:
    def __init__(self, data):
        self.data =data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Check if the value exists, 
        # then you do not need duplicates
        if data == self.data:
            return
        if data < self.data:
            # Left-hand side
            if self.left:
                # If we already have 
                # some value on the left-hand side
                # As BST only has two child elements,
                # we extend the branch
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Righ-hand side
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # In order traversal method - 
    # returns a tree in an ascending order
    def in_order_traversal(self):
        elements = []
        # Examine the left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # Examine the root tree
        elements.append(self.data)
        # Examine the right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False # Value DNE
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False # Value DNE
            
    def find_min(self):
        elements = self.in_order_traversal()
        return elements[0]
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def sum(self):
        elements = self.in_order_traversal()
        sum = 0
        for i in range (0, len(elements)):
            sum += elements[i]
        return sum
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # If the current node is a leaf node (i.e., 
            # it has no left or right child), it returns 
            # None to remove the node from the tree
            if self.left is None and self.right is None:
                return None
            # If the current node has no left child, 
            # it returns the right child to replace 
            # the current node in the tree
            elif self.left is None:
                return self.right
            # If the current node has no right child, 
            # it returns the left child to replace 
            # the current node in the tree
            elif self.right is None:
                return self.left
            # If the current node has both left and 
            # right children, it finds the minimum value 
            # in the right subtree by calling the find_min 
            # method. 
            # It replaces the current node's value with 
            # the minimum value and recursively calls 
            # the delete method on the right child node 
            # to remove the duplicate value.
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root =BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

elements = [8, 4, 7, 2, 13, 7]
build = build_tree(elements) 
build.delete(8)
print(build.in_order_traversal())