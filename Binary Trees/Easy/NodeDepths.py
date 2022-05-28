def nodeDepths(root):
    #Name: Node Depths
	#Category and difficulty: Binary Trees, Easy
    #time: O(n) since we vist each array recursively
	#space: O(n) for the number of recursive calls made
    depth = 0
    sum = 0 + helper(root.left, depth+1) + helper(root.right, depth+1)
    return sum
    pass

def helper(node, depth):
    if(node == None):
        return 0
    return depth + helper(node.left, depth+1) + helper(node.right, depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None