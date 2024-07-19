class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        # print('Level of ', self.value, ' is : ', level)
        spaces = ' ' *3 *level
        ret = (spaces + '|--' + self.value + '\n') if level > 0 else (self.value+'\n')
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    

    
if __name__ == "__main__":
    root = TreeNode("Root")
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")
    child4 = TreeNode('Child 4')

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child1.add_child(child4)

    print(root)