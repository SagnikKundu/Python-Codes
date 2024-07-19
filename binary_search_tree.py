'''--- BINARY SEARCH TREE -----'''

class BinarySearchTree() :
    
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
        
    
    def insert(self, value) :
        if value == self.value :
            return
        
        if value < self.value :
            if self.left :
                self.left.insert(value)
            else :
                self.left = BinarySearchTree(value)
        
        else :
            if self.right :
                self.right.insert(value)
            else :
                self.right = BinarySearchTree(value)
        
        return
    

    def inorder_traversal(self):
        elements = []
        
        if self.left :
            elements += self.left.inorder_traversal()
            
        elements.append(self.value)
        
        if self.right :
            elements += self.right.inorder_traversal()
            
        return elements
    
    
    def search(self, val) :
        if self.value == val :
            return True
        
        if val < self.value :
            if self.left :
                return self.left.search(val)
            else :
                return False
            
        if val > self.value :
            if self.right: 
                return self.right.search(val)
            else:
                return False
            
        
    def find_max(self) :
        if self.right == None :
            return self.value
        return self.right.find_max()
    
    
    def find_min(self) :
        if self.left is None :
            return self.value
        return self.left.find_min()
    
    
    def delete(self, val):
        if val < self.value :
            if self.left :
                self.left = self.left.delete(val)
            else:
                return None
        
        if val > self.value:
            if self.right :
                self.right = self.right.delete(val)
            else:
                return None
            
        else :
            if self.right is None and self.right is None :
                return None 
            if self.right is None:
                return self.left
            if self.left is None :
                return self.right
            
            min_value  = self.right.find_min()
            self.value = min_value
            self.right = self.right.delete(min_value)
            
        return self
    

def build_tree(elements) :
    bst = BinarySearchTree(elements[0])
    
    for i in range(1, len(elements)) :
        bst.insert(elements[i])
        
    return bst
        
        

if __name__ == '__main__' :
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    
    tree = (nums)

    '''
    Example bst :

    17 (Root node)
    |--4 (Left node)
        |--1
        |--9
    |--20 (Right node)
        |--18
        |--23
            |--None
            |--34

    '''
    
    print(tree.inorder_traversal())
    
    search_result = lambda tree, x : f'{x} is present.' if tree.search(x) else f'{x} not found.'
    print(search_result(tree, 4))
    
    tree.delete(20)
    print(tree.inorder_traversal())