def removeIslands(matrix):
    #Name: Remove Islands
	#Category and difficulty: Graphs, Medium
    #time: O(rc), where r and c are the number of rows and columns in the matrix
	#space: O(rc), where r and c are the number of rows and columns in the matrix
    nRows = len(matrix)
    nCols = len(matrix[0])

    

    for row in range(1,nRows-1):
        for col in range(1, nCols-1):
            if(matrix[row][col] == 1):
                #Create aux matrix to check if neighbors have been visited
                visitedMatrix = createVisitedMatrix(nRows, nCols)
                isIsland = True
                
                #Running BFS on current element
                que = [[row, col]]

                while(len(que) > 0):
                    currentIndex = que.pop(0)
                    
                    cRow = currentIndex[0]
                    cCol = currentIndex[1]
                    currentValue = matrix[cRow][cCol]
                    #Set current value as visited
                    visitedMatrix[cRow][cCol] = 1
                    
                    if(currentValue == 1):
                        #Edge condition
                        if((cRow == 0 or cRow == nRows-1 or cCol == 0 or cCol == nCols-1)):
                            isIsland = False
                            break
                        
                        #Add top element if not visited
                        if(cRow-1 >= 0 and visitedMatrix[cRow-1][cCol] == 0):
                            que.append([cRow-1, cCol])
                        #Add top element if not visited
                        if(cRow+1 < nRows and visitedMatrix[cRow+1][cCol] == 0):
                            que.append([cRow+1, cCol])   
                        #Add top element if not visited
                        if(cCol-1 >= 0 and  visitedMatrix[cRow][cCol-1] == 0):
                            que.append([cRow, cCol-1])
                        #Add top element if not visited
                        if(cCol+1 < nCols and  visitedMatrix[cRow][cCol+1] == 0):
                            que.append([cRow, cCol+1])
                
                if(isIsland):
                    matrix[row][col] = 0
    
    return matrix

def createVisitedMatrix(nRows, nCols):
    array = []
    for i in range(nRows):
        array.append([])
        for j in range(nCols):
            array[i].append(0)
    return array    
