def minimumPassesOfMatrix(matrix):
    #Name: Minimum Passes of Matrix
	#Category and difficulty: Graphs, Medium
    #time: O(rc), where r is number of rows and c is number of columns in matrix
    #space: O(rc), where r is number of rows and c is number of columns in matrix

    ## Disclaimer: While the code written here is my own creation, the logic / solution reflected in the code is as explained in the video solutions on AlgoExpert.io, for this problem
    currentQueue = []
    nextQueue = []
    nRows = len(matrix)
    nCols = len(matrix[0])

    #Add positive value positions to currentQueue
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col] > 0):
                currentQueue.append([row, col])
                
    #Track passes of matrix
    nPasses = 0

    #Iterate through postive positions and swap negatives
    while(len(currentQueue) > 0):
        currentIndex = currentQueue.pop(0)

        cRow = currentIndex[0]
        cCol = currentIndex[1]

        #Check and add top value
        if(cRow-1 >= 0):
            if(matrix[cRow-1][cCol] < 0):
                matrix[cRow-1][cCol] *= -1
                nextQueue.append([cRow-1, cCol])

        #Check and add bottom value      
        if(cRow+1 < nRows):
            if(matrix[cRow+1][cCol] < 0):
                matrix[cRow+1][cCol] *= -1
                nextQueue.append([cRow+1, cCol])

        #Check and add left value
        if(cCol-1 >= 0):
            if(matrix[cRow][cCol-1] < 0):
                matrix[cRow][cCol-1] *= -1
                nextQueue.append([cRow, cCol-1])

        #Check and add right value      
        if(cCol+1 < nCols):
            if(matrix[cRow][cCol+1] < 0):
                matrix[cRow][cCol+1] *= -1
                nextQueue.append([cRow, cCol+1])

        #Increase nPasses when current pass complete
        if(len(currentQueue) == 0):
            nPasses += 1
            currentQueue = nextQueue
            nextQueue = []
            
    #Check for remaining negatives after all passes complete
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col] < 0):
                return -1

    return nPasses-1

