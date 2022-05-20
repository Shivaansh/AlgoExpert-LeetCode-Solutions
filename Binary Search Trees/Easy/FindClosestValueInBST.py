def findClosestValueInBst(tree, target):
    #Name: Find closest value in BST
	#Category and difficulty: BSTs, Easy
    #time: O(log n) average, O(n) worst case
	#space: O(1) if solved iteratively, same as time complexity when solved recursively
    
    #initialize and track closest number and current node
	closestNumber = 9999999999
	currentNode = tree
	
    #while current node is not a leaf node
	while(currentNode is not None):

        #check whether to update closestNumber
		currentDifference = abs(currentNode.value - target)
		closestDifference = abs(closestNumber - target)

		#return target if current value == target
		if(currentDifference == 0):
			return target
		
		if(currentDifference < closestDifference):
			closestNumber = currentNode.value
            
		#decide whether to move left or right in BST, using BST property
		if(target < currentNode.value):
			currentNode = currentNode.left
		else:
			currentNode = currentNode.right
			
	return closestNumber
		
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None