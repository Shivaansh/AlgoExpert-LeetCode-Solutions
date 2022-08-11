def numberOfWaysToTraverseGraph(width, height):
    #Name: Number of Ways To Traverse Graph (not optimal)
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(h * w) where h and w are height and width
	#space: O(h * w) where h and w are height and width
    grid = createStoreMatrix(height, width)

    grid[0][0] = 0

    for row in range(1, height):
        for col in range(1, width):
            grid[row][col] = grid[row-1][col] +  grid[row][col-1]

    return grid[-1][-1]

def createStoreMatrix(rows, cols):
    matrix = []
    newArray = []

    for i in range(cols):
        newArray.append(1)

    matrix.append(newArray)

    for i in range(1, rows):
        newArray = [0]*(cols)
        newArray[0] = 1
        matrix.append(newArray)

    return matrix
