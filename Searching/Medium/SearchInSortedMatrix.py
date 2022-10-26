def searchInSortedMatrix(matrix, target):
    #Name: Search in sorted matrix
	#Category and difficulty: Searching, Easy
    #time: O(n + m) if array is unsorted, O(log n) if sorted
	#space: O(1)
    col = len(matrix[0])-1
    row = 0
    while(col >= 0 and row >= 0 and col < len(matrix[0]) and row < len(matrix)):
        current = matrix[row][col]
        if(current == target):
            return [row, col]
        elif(current > target):
            col -= 1
        else:
            row += 1
    return [-1, -1]
