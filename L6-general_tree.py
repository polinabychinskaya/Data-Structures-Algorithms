# We use tree to represent a hierarchy 
# (folder structure) 
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, tree_type, level):
        if self.get_level() > level:
            return
        
        if tree_type == 'both':
            value = self.name + ' ' + self.designation
        elif tree_type == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + value)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(tree_type, level)

def build_tree():
    root = TreeNode('John', 'CEO')

    rd = TreeNode('Mary', 'R&D')
    per1 = TreeNode('Tom', 'Assistant')
    per2 = TreeNode('Perry', 'Assistant')
    rd.add_child(per1)
    rd.add_child(per2)

    fin = TreeNode('Claudia', 'Finance')
    per1 = TreeNode('Ryan', 'Consultant')
    per2 = TreeNode('Anna', 'Accountant')
    fin.add_child(per1)
    fin.add_child(per2)

    root.add_child(rd)
    root.add_child(fin)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree(tree_type='both', level=1)