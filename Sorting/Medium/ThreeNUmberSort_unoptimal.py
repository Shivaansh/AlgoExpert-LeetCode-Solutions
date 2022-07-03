def threeNumberSort(array, order):
    #Name: Three Number Sort
    #Category and difficulty: Sorting, Medium
    #time: O(n^2) since we perform an array insert for n elements
	#space: O(1)
    insertPosition = 0
    for orderNum in order:
        print(insertPosition)
        for index in range(len(array)):
            if(array[index] == orderNum):
                #Array mutations are an O(n) operation and these run a max of n times
                array.pop(index)
                array.insert(insertPosition, orderNum)
                
        newIndex = insertPosition
        while(newIndex < len(array) and array[newIndex] == orderNum):
            newIndex += 1
        insertPosition = newIndex
    return array
