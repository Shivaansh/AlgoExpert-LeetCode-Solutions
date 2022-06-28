def invertBinaryTree(tree):
    #Name: Invert Binary Tree
    #Category and difficulty: Binary Trees, Medium
    #time: O(n) since we vist each node
    #space: O(d) for depth of the tree

    queue = [tree]
    #BFS-like approach
    while(len(queue) > 0):
        current = queue.pop(0)
        #Swap children of current node
        temp = current.left
        current.left = current.right
        current.right = temp
        #add children to queue
        if(current.left is not None):
            queue.append(current.left)
        if(current.right is not None):
            queue.append(current.right)
            
    return tree
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
