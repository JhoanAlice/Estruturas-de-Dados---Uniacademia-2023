import abc
import sys

class Tree(metaclass=abc.ABCMeta): 

     @abc.abstractmethod
     def clear(self):
         pass

     @abc.abstractmethod
     def copy(self):
         pass

     @abc.abstractmethod
     def root(self):
          pass

     @abc.abstractmethod
     def isEmpty(self):
          pass

     @abc.abstractmethod
     def parent(self,element):
          pass

     @abc.abstractmethod
     def get(self, element):
          pass         
     
class treeNode:
     def __init__(self,element):
        self.element = element
        self.child = None
        self.sibling = None

     def __str__(self):
          """Returns a string representation"""
          return str(self.element)

     def __repr__(self):
          """Returns a representation"""
          return repr(self.element)

     def get_element(self):
          return self.element


class abstractTree(Tree): 
                      
     # concrete methods     
     def isEmpty(self):
        return len(self) == 0

     def root(self):
        return self._root

     def __repr__(self):
        """Returns a representation"""
        return type(self).__name__+"-> "+str(self)

     def __ne__(self,other):
        return not self == other

class binaryTreeNode:
     def __init__(self,element):
        self.element = element
        self.left = None
        self.right = None

     def __str__(self):
          return str(self.element)

     def __repr__(self):
          return str(self.element)

     def get_element(self):
          return self.element

class binaryTree(abstractTree):
    def __init__(self):
        self._root = None
        self._size = 0

    def clear(self):
        self.__init__()
        
    def __contains__(self,element):
         return True if self._get(element) else False

    def __len__(self):
         return self._size

    def __iter__(self):
         return iter(self.inOrder())

    def __str__(self):
         return str(self.inOrder())

    def __eq__(self,other):
        if type(self) == type(other): 
            return self.inOrder() == other.inOrder()
        return False
          
    def get(self, element):
         """Returns Node if elemet is found or None otherwise."""
         return self._get(element)
         
    def _get(self, element):
         # returns node if node.element == element else None
         found = False
         def bodyget(root,element,found):
             node = root
             if root:
                 if(root.get_element() == element):
                     found=True
                     return root
                 node=bodyget(root.left,element,found)
                 if not node:
                     node=bodyget(root.right,element,found)
             return node
         node = bodyget(self._root,element,found)
         return node
         
    def insertRoot(self,element):     
        if self._root:  # Tree not empty
            raise TypeErrror('tree not is empty')
        self._root = binaryTreeNode(element)
        self._size += 1
         
    def insertLeft(self,currNode,element):     
        if currNode == None: # insert root
            raise TypeErrror('parent is None or tree is empty')
        else:
            if currNode.left:
                currNode.left.element = element  # update node
            else:
                currNode.left = binaryTreeNode(element) # new node
        self._size += 1
        
    def insertRight(self,currNode,element):     
        if currNode == None: # insert root
            raise TypeErrror('parent is None or tree is empty')
        else:
            if currNode.right == element:   # update node
                currNode.right.element = element
            else:
                currNode.right = binaryTreeNode(element) # new node
        self._size += 1

    def remove(self, element): 
        if not (element in self):
            raise TypeError(str(element)+ ' not in Tree')
        self._size -=1
        self._root=self._delete(self._root,element)
        return element
    
    # Recursive function to delete a node with 
    # given element from subtree with given root. 
    # It returns root of the modified subtree. 
    def _delete(self, root, element): 
        # Step 1 - Perform normal Binary Tree   
        if not root: 
            return root 
        elif element != root.element: 
            root.left = self._delete(root.left, element)
            root.right = self._delete(root.right, element) 
        else: 
            # cases 1 or 2 : node is leaf or has one child
            if root.left is None: 
                temp = root.right 
                root = None
                return temp   
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            # caso 3 - node with two children
            temp = self._successor(root.right) 
            root.element = temp.element
            root.right = self._delete(root.right, 
                                      temp.element) 
        return root

    # Recusive function return-> predecessor node
    def _predecessor(self,node): 
        if(node.right != None ):
            return self._predecessor(node.right)
        return node
    
    # Recusive function return-> successor node    
    def _successor(self,node): 
        if(node.left != None ):
            return self._successor(node.left)
        return node
    
    #def isEmpty(self):
    #    return self._root == None

    def show(self):
        # adapted from https://www.worldofitech.com/red-black-tree-insertion/
        self._show(self._root, "", True)

    # Printing the tree
    def _show(self, node, indent, last):
        # adapted from https://www.worldofitech.com/red-black-tree-insertion/
        if node != None:
            sys.stdout.write(indent)
            if last:
                if node == self._root:
                    sys.stdout.write("Root.")
                else:    
                    sys.stdout.write("R..")
                indent += "   "
            else:
                sys.stdout.write("L..")
                indent += "   "
            print(str(node.get_element()))
            self._show(node.left, indent, False)
            self._show(node.right, indent, True)


    def parent(self, element):
         """returns the node if the parent of the element exists and None otherwise"""
         if not (element in self):
            raise TypeError(str(element)+ ' not in Tree')
         global parent,found
         parent = None
         found =False         
         def body(node):
             global parent,found
             if node != None:
                 if node.element==element:
                      node = None
                      found = True
                 else:
                      if found:
                           return
                      if(node.left):
                          parent = node
                          body(node.left)
                      if found:
                           return   
                      if(node.right):
                          parent =node
                          body(node.right)
             return 
         body(self.root())
         return parent
         
    def preOrder(self):
         """Supports an preOrder traversal on a view of self."""
         tr = []
         def bodyPreOrder(root):
             if root:
                 tr.append(root.get_element())
                 bodyPreOrder(root.left)
                 bodyPreOrder(root.right)
             return tr
   
         return bodyPreOrder(self._root)
          
    def posOrder(self):
         """Supports an posOrder traversal on a view of self."""
         tr = []
         def bodyPosOrder(root):
             if root:
                 bodyPosOrder(root.left)
                 bodyPosOrder(root.right)
                 tr.append(root.get_element())
             return tr

         return bodyPosOrder(self._root)
     
    def inOrder(self):
         """Supports an inOrder traversal on a view of self."""
         tr = []
         def bodyInOrder(root):
             if root:
                 bodyInOrder(root.left)
                 tr.append(root.get_element())
                 bodyInOrder(root.right)          
             return tr

         return bodyInOrder(self._root)

    def copy(self):
        cp = binaryTree()
        cp.insertRoot(self.root().element)
        def _copy(node):
            if node != None:
                 if(node.left):
                     cp.insertLeft(cp.get(node.get_element()),node.left.get_element()) 
                     _copy(node.left)
                 if(node.right):
                     cp.insertRight(cp.get(node.get_element()),node.right.get_element()) 
                     _copy(node.right)
        _copy(self.root())
        return cp

class BSTNode(): 
    def __init__(self, key,value):
        self.key = key
        self.value = value 
        self.left = None 
        self.right = None 

    def get_element(self):
        return (self.key,self.value)
    
    def __str__(self):
        return str((self.key,self.value))

    def __repr__(self):
        return str(self)

class bst(binaryTree):
    def __init__(self,items=None):
        super().__init__()
        if items:
            entries=[]
            if(type(items) is list):
                entries = items                    
            elif(type(items) is dict):
                entries = items.items()
            elif(type(items) is bst or type(items) is avl):
                entries = items.items()
            else:
                raise TypeError("'"+type(items).__name__+"'"+ \
                                ' object is not iterable')
            for k,v in entries:
                self.put(k,v)

    def __iter__(self):
        return iter(self.items())

    def __eq__(self,other):
        if type(self) == type(other): 
            return self.items() == other.items()
        return False

    def __add__(self,other):
        t = self.copy()
        t.extend(other.items())
        return t

    def __sub__(self,other):
        t = self.copy()
        for k in other.keys():
            if k in t:
                t.remove(k)
        return t

    def __contains__(self,key):
        if isinstance(key,tuple):
            return self.find(key[0])and key == (key[0],self.get(key[0]))
        return self.find(key)

    def contains(self,key):
        return key in self

    def __getitem__(self, key): 
       if (type(key) is slice):
            raise TypeError("unhashable type: 'slice'")
       if key in self:
           return self.get(key)
       raise KeyError("key not in Tree")
         
    def __delitem__(self, key):
        if not key in self:
            raise KeyError("key not in Tree")
        return self.remove(key)      

    def __setitem__(self, key,value):
        self.put(key,value)
    
    def __str__(self):
        return str(dict(self))
     
    # function to insert key, value in BST  
    def put(self,key,value):
        self._size += 1
        self._root=self._insert(self._root,key,value)
        
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def _insert(self, root, key,value):
         
        # Step 1 - Perform normal BST 
        if root==None: 
            return BSTNode(key,value) 
        elif key < root.key: 
            root.left = self._insert(root.left, key,value) 
        elif key > root.key: 
            root.right = self._insert(root.right, key,value)
        else:
            self._size -= 1        
            # key equal, replace value
            root.value = value
        return root 

    def pop(self,key):
        return self.remove(key)    
    
    def remove(self,key):        
        if not (key in self):
            raise KeyError('key not in self')
        self._root=self._delete(self._root,key)
        return key    

    # Recursive function to delete a node with 
    # given key from subtree with given root. 
    # It returns root of the modified subtree. 
    def _delete(self, root, key): 
        # Step 1 - Perform normal BST   
        if not root: 
            root 
        elif key < root.key: 
            root.left = self._delete(root.left, key)  
        elif key > root.key: 
            root.right = self._delete(root.right, key) 
        else: 
            # cases 1 or 2 : node is leaf or has one child
            if root.left is None: 
                temp = root.right 
                root = None
                return temp   
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            # caso 3 - node with two children
            temp = self._successor(root.right) 
            root.key = temp.key
            root.value = temp.value
            
            root.right = self._delete(root.right,temp.key)

        return root

    def _rec_get(self,root,key):
        if root==None:
            return root
        if key < root.key:
            return self._rec_get(root.left, key) 
        elif key > root.key: 
            return self._rec_get(root.right, key) 
        else: 
            return root
        
    def get(self, key): 
        """Returns value if key is found or None otherwise."""
        node = self._rec_get(self._root,key)
        if not node:
            return None
        return node.value     
        
    def find(self,key):
        return not self._rec_get(self._root,key) == None     
        
    def keys(self):
        return [key for key,value in self.items()]

    def values(self):
        return [value for key,value in self.items()]
        
    def entries(self):
        return self.items()
    
    def items(self):
        return self.inOrder()
                
    def copy(self):
        return bst(self.items())

    def update(self,iterable):
        return self.extend(iterable)

    def parent(self, key):
        if not (key in self):
            raise KeyError('key not in self')
        global parent
        parent =None
        def getParent(root,key):
             global parent
             if root==None:
                 return 
             if key < root.key:
                 parent = root
                 getParent(root.left, key) 
             elif key > root.key: 
                 parent = root
                 getParent(root.right, key) 
             else: 
                 return root            
        getParent(self._root,key)
        return parent     
    
    def extend(self,iterable):
        entries=[]
        if(type(iterable) is list):
             entries = iterable
        elif(type(iterable) is dict):
             entries = iterable.items()
        elif(type(iterable) is bst or type(iterable) is avl or type(iterable) is redBlackTree):
             entries = iterable.items()
        else:
             raise TypeError("'"+type(iterable).__name__+"'"+' object is not iterable')
        for k,v in entries:
             self.put(k,v)

    def insertRoot(self,entry='This method is not implemented in the subclass'):
        print('This method is not implemented in the subclass')
        pass

    def insertLeft(self,entry='This method is not implemented in the subclass'):
        print('This method is not implemented in the subclass')
        pass

    def insertRight(self,entry='This method is not implemented in the subclass'):
        print('This method is not implemented in the subclass')
        pass

class AVLNode(BSTNode): 
    def __init__(self, key,value): 
        super().__init__(key,value)
        self.height = 1
        

class avl(bst):    
    def __init__(self,items=None): 
        super().__init__(items) 

    # function to insert key, value in AVL  
    def put(self,key,value):
        self._size += 1
        self._root=self._insert(self._root,key,value)

    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def _insert(self, root, key,value):
        # adapted from https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
        # Step 1 - Perform normal BST 
        if root==None: 
            return AVLNode(key,value) 
        elif key == root.key:
            self._size -= 1        
            root.value = value 
            return root        
        elif key < root.key: 
            root.left = self._insert(root.left, key,value) 
        else: 
            root.right = self._insert(root.right, key,value) 
        # Step 2 - Update the height of the ancestor node 
        root.height = 1 + max(self._getHeight(root.left), 
                           self._getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self._getBalance(root) 
  
        # Step 4 - If the node is unbalanced, then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.key: 
            #print('LL')
            return self._rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.key: 
            #print('RR')        
            return self._leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.key: 
            #print('LR')        
            root.left = self._leftRotate(root.left) 
            return self._rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.key: 
            #print('RL')        
            root.right = self._rightRotate(root.right) 
            return self._leftRotate(root) 
  
        return root 
  
    def _leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self._getHeight(z.left), 
                         self._getHeight(z.right)) 
        y.height = 1 + max(self._getHeight(y.left), 
                         self._getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def _rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self._getHeight(z.left), 
                        self._getHeight(z.right)) 
        y.height = 1 + max(self._getHeight(y.left), 
                        self._getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def _getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def _getBalance(self, root): 
        if not root: 
            return 0
  
        return self._getHeight(root.left) - self._getHeight(root.right) 
  
    # Recursive function to delete a node with 
    # given key from subtree with given root. 
    # It returns root of the modified subtree. 
    def _delete(self, root, key):

        # Step 1 - Perform normal AVL   
        if not root: 
            return root 
        elif key < root.key: 
            root.left = self._delete(root.left, key) 
        elif key > root.key: 
            root.right = self._delete(root.right, key) 
        else:
            # cases 1 or 2 : node is leaf or has one child
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
            # caso 3 - node with two children
            temp = self._successor(root.right) 
            root.key = temp.key
            root.value = temp.value 
            root.right = self._delete(root.right, 
                                      temp.key) 
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self._getHeight(root.left), 
                            self._getHeight(root.right)) 
        # Step 3 - Get the balance factor 
        balance = self._getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self._getBalance(root.left) >= 0:
            #print('LL')
            return self._rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self._getBalance(root.right) <= 0: 
            #print('RR')
            return self._leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self._getBalance(root.left) < 0: 
            #print('LR')
            root.left = self._leftRotate(root.left) 
            return self._rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self._getBalance(root.right) > 0: 
            #print('RL')
            root.right = self._rightRotate(root.right) 
            return self._leftRotate(root) 
  
        return root

    def copy(self):
        return avl(self.items())        

        
if __name__ == '__main__':
     """          
     t = avl()
     t.put(20,'ana')
     t.put(30,'bia')
     t.put(10,'leila')
     t[5]='lucas'
     t[35]='gabriel'
     t[15]='hugo'
     t[25]='fred'
     """     
     t = bst()
     t.put(20,'ana')
     t.put(30,'bia')
     t.put(10,'leila')
     t.put(25,'maria')
     t.put(50,'carlos')
     """
     bt=binaryTree()
     bt.insertRoot(20)
     bt.insertLeft(bt.root(),10)
     bt.insertRight(bt.root(),30)
     bt.insertRight(bt.root().right,40)
     bt.show()
     """     
         



