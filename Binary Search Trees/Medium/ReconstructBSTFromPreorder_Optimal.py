# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#Name: Reonstruct BST (from Preorder traversal)
#Category and difficulty: BSTs, Medium
#Note: This is the most optimal solution
def reconstructBst(preOrderTraversalValues):
    #time: O(n) for each element of the traversal
    #space: O(n) for space used by array / maximum space used by stack
    head = BST(preOrderTraversalValues[0])
    pointer = head
    stack = [pointer]
    index = 1
    while(index < len(preOrderTraversalValues)):
        value = preOrderTraversalValues[index]
        if(value < pointer.value):
            stack.append(pointer)
            pointer.left = BST(value)
            index += 1
            pointer = pointer.left
        elif(value >= pointer.value):
            if(len(stack) == 0):
                pointer.right = BST(value)
                index += 1
                pointer = pointer.right
            elif(value < stack[-1].value):
                pointer.right = BST(value)
                index += 1
                pointer = pointer.right
            else:
                pointer = stack.pop()
    return head
