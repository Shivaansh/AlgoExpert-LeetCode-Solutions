def nextGreaterElement(array):
    #Name: Sort Stack
    #Category and difficulty: Stack, Medium
    #time: O(n) as we go through max 2 iterations of the array
	#space: O(n) for max depth of
    if(len(array) == 0):
        return []

    toFindStack = []
    outArray = [-1] * len(array)
    
    #Condition: We can definitely find next max for all numbers in 2 passes
    for index in range(2 * len(array)):
        
        #Rotating array
        currIndex = index % len(array)
        currentNumber = array[currIndex]

        #If current > top of stack then next max for that number has been found so remove from stack
        while(len(toFindStack) != 0 and currentNumber > array[toFindStack[-1]]):
            outArray[toFindStack.pop()] = currentNumber
        #Add current to stack since the next max has not been found
        toFindStack.append(currIndex)

    return outArray
