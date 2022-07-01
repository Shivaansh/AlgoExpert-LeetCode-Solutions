# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Name: Construct  BST
#Category and difficulty: BSTs, Medium

    def insert(self, value):
        #time: O(log n) on average, where n is number of nodes in tree
	    #space: O(1) since this is an iterative appraoch
        # Do not edit the return statement of this method.
        head = self
        tail= None
        newNode = BST(value)
        while(head is not None):
            tail = head
            if(head.value <= value):
                head = head.right
            elif(head.value > value):
                head = head.left
        if(value < tail.value):
            tail.left = newNode
        elif(value >= tail.value):
            tail.right = newNode
        return self

    def contains(self, value):
        #time: O(log n) on average, where n is number of nodes in tree
	    #space: O(1) since this is an iterative appraoch
        pointer = self
        while(pointer is not None):
            if(pointer.value == value):
                return True
            elif(pointer.value > value):
                pointer = pointer.left
            else:
                pointer = pointer.right
        return False

    def remove(self, value, parent = None):
        #time: O(log n) on average, where n is number of nodes in tree
	    #space: O(1) since this is an iterative appraoch
        # Do not edit the return statement of this method.
        current = self
        while(current is not None):
            #When not found node to remove
            if(current.value > value):
                parent = current
                current = current.left
            elif(current.value < value):
                parent = current
                current = current.right
            else:
            #When current node has value to be removed
                #If target node has 2 children, doesn't matter if root or not
                if(current.left is not None and current.right is not None):
                    #Replace value of current with value of InOrder successor
                    current.value = current.getInorderSuccessorValue()
                    #Now that current is updated, we remove the InOrder Successor by calling Remove on the right subtree
                    current.right.remove(current.value, current)
                #If target node is a root node with 0 or 1 child
                elif(parent is None):
                    #Single child, child is a left node
                    if(current.left is not None):
                        current.value = current.left.value
                        current.right = current.left.right
                        current.left = current.left.left
                    #Single child, child is a left node
                    elif(current.right is not None):
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    #Root node with no children
                    else:
                        pass
                #If current node is a left child of parent node, current node has 0 or 1 child
                elif(current == parent.left):
                    if(current.left is not None):
                        parent.left = current.left
                    else:
                        parent.left = current.right
                #If current node is a right child of parent node, current node has 0 or 1 child
                elif(current == parent.right):
                    if(current.left is not None):
                        parent.right = current.left
                    else:
                        parent.right = current.right
                break
        return self

    #time: O(log n) on average, where n is number of nodes in tree
	#space: O(1) since this is an iterative appraoch
    def getInorderSuccessorValue(self):
        head = self.right
        while(head.left is not None):
            head = head.left
        return head.value

