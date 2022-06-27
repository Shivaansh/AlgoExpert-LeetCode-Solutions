def riverSizes(matrix):
    #Name: River Sizes
	#Category and difficulty: Graphs, Medium
    #time: O(rc), where r and c are the number of rows and columns in the matrix
	#space: O(rc), where r and c are the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    sizes = []
    for row in range(0, rows):
        for col in range(0, cols):
            if(matrix[row][col] == 1):
                #Mark as seen and set size = 1
                size = 0
                queue = [[row, col]]
                
                while(len(queue) > 0):
                    current = queue.pop(0)
                    cRow = current[0]
                    cCol = current[1]
                    
                    if(matrix[cRow][cCol] == 1):
                        matrix[cRow][cCol] = -1
                        size += 1

                        #Add top
                        if(cRow-1 >= 0):
                            queue.append([cRow-1, cCol])
                        
                        #Add bottom
                        if(cRow+1 < rows):
                            queue.append([cRow+1, cCol])

                        #Add left
                        if(cCol-1 >= 0):
                            queue.append([cRow, cCol-1])
                        
                        #Add bottom
                        if(cCol+1 < cols):
                            queue.append([cRow, cCol+1])
    
                sizes.append(size)
                
    return sizes                
    pass
