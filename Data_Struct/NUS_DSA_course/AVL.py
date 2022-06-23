from enum import Enum


"""
Adapted for DS&A Part II - by SYJ

Version 1.1 (2022 June)
- Removed inheritance and abstract methods

For IT5003 - by SYJ 

Version 1.0 (2019 October)
- AVL ADT implemented using reference as a BST subclass
- AVLNode class for the reference based tree node

** Student Version **
- Certain method is left empty for your own practice
- Basic documentation only

"""
class Traversal(Enum):
    """
    Enumeration for more readable code.

    Represent the four possible Binary Tree Traversals.
    """
    IN = 1
    PRE = 2
    POST = 3
    LEVEL = 4

class AVLNode:
    """
    Reference based AVL Binary Tree Node.
    """
    def __init__(self, key, data, leftPtr = None, rightPtr = None):
        """
        [key] and [data] are expected.

        Has additional attribute height to aid AVL Tree operations.
        """
        self.key = key
        self.data = data
        self.height = 1 #for calculating balance factor
        self.leftT = leftPtr
        self.rightT = rightPtr
    
    def _getHeights(self):
        """
        Helper method to get the heights of left, right subtree.

        Return a tuple (left height, right height).
        """
        Hleft = Hright = 0

        if self.leftT != None:
            Hleft = self.leftT.height
        
        if self.rightT != None:
            Hright = self.rightT.height
        
        return (Hleft, Hright)

    def balanceFactor(self):
        """
        Helper method to return the balance factor at this node.

        Return [left subtree height - right subtree height].
        """
        Hleft, Hright = self._getHeights()
        return Hleft - Hright
    
    def updateHeight(self):
        """
        Helper method to update the height of this node.
        """
        Hleft, Hright = self._getHeights()
        self.height = (Hleft if Hleft > Hright else Hright) + 1

    def toString(self):
        return "[K:%d|Data%s|Depth%d | left at %d |right at %d]"%(self.key, self.data, self.depth, self.leftT, self.rightT)


class AVLTree:
    """
    AVL Tree implemented with reference
    """
    def __init__(self):
        """
        Returns an empty AVL Tree
        """
        self._root = None
        self._size = 0  
   
    def _rotateRight(self, x):
        """ 
        Helper method to perform right rotation at node x.

        Return the rotated tree.
        """
        l = x.leftT
        if l == None:   #cannot rotate!
            return x
        x.leftT = l.rightT
        l.rightT = x

        x.updateHeight()
        l.updateHeight()
        return l
    
    def _rotateLeft(self, x):
        """ 
        Helper method to perform left rotation at node x.

        Return the rotated tree.
        """
        r = x.rightT
        if r == None:   #cannot rotate!
            return x
        x.rightT = r.leftT
        r.leftT = x

        x.updateHeight()
        r.updateHeight()
        return r

    def _balance(self, T):
        """
        Helper method to perform AVL balancing at node T.

        Return a balanced AVL tree.
        """
        if T == None:
            return None
    
        T.updateHeight()
        BF = T.balanceFactor()

        # print("At %d | BF = %d"%(T.key, BF))

        # Check Balance Factor and perform rotations if necessary
        # Incomplete:
        #   Check the Balance factor, call the necessary rotation(s) to correct the issue

        return T

    def _insert(self, T, key, data ):
        """
        Internal recursive method that carries out the insertion algorithm.

        Perform AVL Balancing after insertion.
        """
        if T == None:
            return AVLNode( key, data )
        
        if T.key == key:
            raise KeyError("Duplicate Key!")
        elif T.key < key:
            T.rightT = self._insert( T.rightT, key, data )
        else:
            T.leftT  = self._insert( T.leftT, key, data )
        
        return self._balance(T)

    def insert(self, key, data):
        """
        Insert (key, data) into AVL Tree.

        [key] is used to determine the location of the insertion.
        """
        self._root = self._insert(self._root, key, data)
        self._size += 1

    def _delete( self, T, key ):
        """
        Internal recursive method that carries out the deletion algorithm.

        Perform AVL Balancing after deletion.
        """

        #Incomplete:
        #   Complete the BST deletion first
        #   Take a look at how insertion perform balancing 
        #   (hint: just a one line change from BST --> AVL)
        return T   

    def delete(self, key):
        """
        Detele node with [key] from AVL Tree.
        """
        self._root = self._delete( self._root, key)
        self._size -= 1

    #*************************************************
    #The following functions are duplicated code     *
    #  from BSTRef class. Can use inheritance to     *
    #  reduce redundancy                             *
    #*************************************************

    def _preorder(self, T):
        """
        Internal recursive method to perform Pre-Order Traversal.
        """
        if T == None:
            return "-"
        return "{ %s "%(T.key) + self._preorder(T.leftT) \
            + " " + self._preorder(T.rightT) + " } "

    def _inorder(self, T):
        """
        Internal recursive method to perform In-Order Traversal.
        """
        return "" #Incomplete Implementation

    def _postorder(self, T):
        """
        Internal recursive method to perform Post-Order Traversal.
        """
        return "" #Incomplete Implementation

    def traversal(self, which):
        """
        Print the BST by the specified traversal.

        [which] should be one of the Enumeration in the Traversal Enum class
        """
        if which == Traversal.PRE:
            return "[%d nodes]="%self._size+self._preorder(self._root) 
        elif which == Traversal.IN:
            return "[%d nodes]="%self._size+self._inorder(self._root)
        elif which == Traversal.POST:
            return "[%d nodes]="%self._size+self._postorder(self._root)

def buildTree( L ):
    """
    Utility Function to build a tree by inserting the number in the list [L].

    Return AVL Tree
    """
    avlT = AVLTree()
    for item in L:
        avlT.insert(item, str(item))
    
    return avlT

def main():
    """
    #Examples:
    Right skewed: Double Rotation 7, 4, 9, 5, 8, 13, 12, 15, 11
    Left skewed: Double Rotation 7, 4, 9, 1, 5,  8,  0,  2,  3
    """

    # Test AVL insertion
    avlT = buildTree([7, 4, 9, 5, 8, 13, 12, 15])
    print(avlT.traversal(Traversal.PRE))
    while True:
        key = int(input("Key to insert: "))
        avlT.insert(key, str(key))
        print(avlT.traversal(Traversal.PRE))

    # Test AVL deletion
    # avlT = buildTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    # print(avlT.traversal(Traversal.PRE))
    # while True:
    #     key = int(input("Key to delete: "))
    #     avlT.delete(key)
    #     print(avlT.traversal(Traversal.PRE))

    

if __name__ == "__main__":
    main()