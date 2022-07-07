def staircaseTraversal(height, maxSteps):
    #Name: Staircase Traversal
	#Category and difficulty: Recursion, Medium
    #time: O(kh) where k is maxsteps allowed and h is height of staircase
	#space: O(h) for depth of recursive stack
    totalWays = [1]
    staircaseTraversalHelper(height, maxSteps, totalWays)
    return len(totalWays)-1

#Can run max kh times because if maxStep is 1, then can take h steps
def staircaseTraversalHelper(heightLeft, maxSteps, totalWays):
    if(heightLeft == 0):
        totalWays.append(1)
    else:
        for stepLength in range(1, maxSteps+1):
            if(heightLeft-stepLength >= 0):
                staircaseTraversalHelper(heightLeft-stepLength, maxSteps, totalWays)
