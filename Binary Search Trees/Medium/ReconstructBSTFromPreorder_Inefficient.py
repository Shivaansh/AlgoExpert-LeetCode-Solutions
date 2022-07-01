# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#Name: Reonstruct BST (from Preorder traversal)
#Category and difficulty: BSTs, Medium
#Note: This is NOT the most optimal solution, but is quite easy to implement
def reconstructBst(preOrderTraversalValues):
    #time: O(n log n) on average, since we run an O(log n) approach ~n times
    #space: O(n) for space used by array
    head = BST(preOrderTraversalValues[0])
    for index in range(1, len(preOrderTraversalValues)):
        insert(head, preOrderTraversalValues[index])
    return head

#time: O(log n) on average, where n is number of nodes in tree
#space: O(1) since this is an iterative appraoch
def insert(root, value):
    current = root
    tail = None
    newNode = BST(value)
    while(current is not None):
        tail = current
        if(current.value > value):
            current = current.left
        else:
            current = current.right
    if(newNode.value < tail.value):
        tail.left = newNode
    else:
        tail.right = newNode
    return root
