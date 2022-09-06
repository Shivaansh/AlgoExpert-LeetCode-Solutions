def zigzagTraverse(array):
    #Name: Zigzag Traverse
	#Category and difficulty: Arrays, Hard
    #time: O(n * m) where n * m is the size of matrix
	#space: O(n * m) where n * m is the size of matrix
    firstRow = 0
    firstCol = 0
    lastRow = len(array)-1
    lastCol = len(array[0])-1
    directionUp = True
    currentRow = 1
    currentCol = 0

    #EDGE Case: if only containing one row
    if(len(array) == 1):
        return array[0]

    returnArray = []
    returnArray.append(array[0][0])

    while(currentRow >= 0 and currentCol >= 0 and currentRow < len(array) and currentCol < len(array[0])):
        returnArray.append(array[currentRow][currentCol])

        if(directionUp):
            #Going UP
            if(currentRow == firstRow or currentCol == lastCol):
                directionUp = False
                if(currentCol == lastCol):
                    currentRow += 1
                elif(currentRow == firstRow):
                    currentCol += 1
            else:
                currentRow -= 1
                currentCol += 1
        else:
            #Going DOWN
            if(currentRow == lastRow or currentCol == firstCol):
                directionUp = True
                if(currentRow == lastRow):
                    currentCol += 1
                elif(currentCol == firstCol):
                    currentRow += 1
            else:
                currentRow += 1
                currentCol -= 1
    return returnArray
