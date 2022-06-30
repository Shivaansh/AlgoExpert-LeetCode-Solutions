#Name: Traverse BST
#Category and difficulty: BSTs, Medium

def inOrderTraverse(tree, array):
    #InOrder traversal = left -> parent -> right
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    if(tree is not None):
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    #PreOrder traversal = parent -> left -> right
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    if(tree is not None):
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    #PostOrder traversal = left -> right -> parent
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    if(tree is not None):
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

