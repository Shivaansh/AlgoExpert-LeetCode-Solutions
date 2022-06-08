def spiralTraverse(array):
    #Name: Spiral Traversal
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we sort go through all the values in the input array once
	#space: O(n) since the returned array has size same as input array
    spiralTraversal = []
    startRow = 0
    endRow = len(array)-1
    startCol = 0
    endCol = len(array[0])-1

    #Using perimeter approach to solve for rectangles
    while(startRow <= endRow and startCol <= endCol):
        #top row
        for colIndex in range(startCol, endCol+1):
            spiralTraversal.append(array[startRow][colIndex])
        #Right column
        for rowIndex in range(startRow+1, endRow+1):
            spiralTraversal.append(array[rowIndex][endCol])
        #bottom row in reverse
        for revColIndex in reversed(range(startCol, endCol)):
            if(startRow == endRow):
                break
            spiralTraversal.append(array[endRow][revColIndex])

        #left column in reverse
        for revRowIndex in reversed(range(startRow+1, endRow)):
            if(startCol == endCol):
                break
            spiralTraversal.append(array[revRowIndex][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
        
    return spiralTraversal
    pass
