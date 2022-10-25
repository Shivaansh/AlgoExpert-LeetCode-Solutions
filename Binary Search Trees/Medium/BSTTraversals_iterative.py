#Name: Traverse BST
#Category and difficulty: BSTs, Medium

def inOrderTraverse(tree, array):
    #InOrder traversal = left -> parent -> right
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    stack = []
    temp = tree
    while(temp is not None or len(stack)>0):
        if(temp is not None):
            stack.append(temp)
            temp = temp.left
        else:
            if(len(stack) > 0):
                temp = stack.pop()
                array.append(temp.value)
                temp = temp.right
    return array


def preOrderTraverse(tree, array):
    #PreOrder traversal = parent -> left -> right
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    stack = []
    temp = tree
    while(temp is not None or len(stack)>0):
        if(temp is not None):
            array.append(temp.value)
            stack.append(temp)
            temp = temp.left
        else:
            if(len(stack) > 0):
                temp = stack.pop()
                temp = temp.right
    return array

def postOrderTraverse(tree, array):
    #PostOrder traversal = left -> right -> parent
    #time: O(n) where n is number of nodes in tree
	#space: O(n) for space used by array
    stack = []
    temp = tree
    while(temp is not None or len(stack)>0):
        while(temp is not None):
            if(temp.right is not None):
                stack.append(temp.right)
            stack.append(temp)
            temp = temp.left
            
        if(len(stack) > 0):   
            temp = stack.pop()
        if(temp is not None and temp.right is not None and len(stack) > 0 and temp.right == stack[-1]):
            stack.pop()
            stack.append(temp)
            temp = temp.right
        else:
            array.append(temp.value)
            temp = None
    return array

