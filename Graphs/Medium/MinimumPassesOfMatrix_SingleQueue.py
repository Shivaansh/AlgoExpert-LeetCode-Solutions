def minimumPassesOfMatrix(matrix):
    #Name: Minimum Passes of Matrix
	#Category and difficulty: Graphs, Medium
    #time: O(rc), where r is number of rows and c is number of columns in matrix
    #space: O(rc), where r is number of rows and c is number of columns in matrix

    ## Disclaimer: While the code written here is my own creation, the logic / solution reflected in the code is as explained in the video solutions on AlgoExpert.io, for this problem
    ## Here we only use one queue and track the number of new elements added to the queue in each pass
    queue = []
    nRows = len(matrix)
    nCols = len(matrix[0])

    #Add positive value positions to queue
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col] > 0):
                queue.append([row, col])
                
    #Track passes of matrix
    nPasses = 0
    size = len(queue)
    count = 0
    newSize = 0

    #Iterate through postive positions and swap negatives
    while(count < size):
        currentIndex = queue.pop(0)
        count += 1

        cRow = currentIndex[0]
        cCol = currentIndex[1]

        #Check and add top value
        if(cRow-1 >= 0):
            if(matrix[cRow-1][cCol] < 0):
                matrix[cRow-1][cCol] *= -1
                queue.append([cRow-1, cCol])
                newSize += 1

        #Check and add bottom value      
        if(cRow+1 < nRows):
            if(matrix[cRow+1][cCol] < 0):
                matrix[cRow+1][cCol] *= -1
                queue.append([cRow+1, cCol])
                newSize += 1

        #Check and add left value
        if(cCol-1 >= 0):
            if(matrix[cRow][cCol-1] < 0):
                matrix[cRow][cCol-1] *= -1
                queue.append([cRow, cCol-1])
                newSize += 1

        #Check and add right value      
        if(cCol+1 < nCols):
            if(matrix[cRow][cCol+1] < 0):
                matrix[cRow][cCol+1] *= -1
                queue.append([cRow, cCol+1])
                newSize += 1

        #Increase nPasses when current pass complete
        if(count == size):
            size = newSize
            newSize = 0
            count = 0
            nPasses += 1

            
    #Check for remaining negatives after all passes complete
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col] < 0):
                return -1

    return nPasses-1

