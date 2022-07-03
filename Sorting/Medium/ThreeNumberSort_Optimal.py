def threeNumberSort(array, order):
    #Name: Three Number Sort
    #Category and difficulty: Sorting, Medium
    #time: O(n) 
	#space: O(1)

    #track counts of each element in the order
    #can use three distinct variables but easier to use an array of length 3, this would still effectively be O(1)
    elementCounts = [0, 0, 0]

    for index in range(len(order)):
        #making 3 passes through array
        for element in array:
            if(element == order[index]):
               elementCounts[index] += 1


    position = 0
    #replace values in array
    for val in range(len(order)):
        count = elementCounts[val]
        numToInsert = order[val]
        switches = 0
        while(position < len(array) and switches < count):
            array[position] = numToInsert
            switches += 1
            position += 1
    
    return array
    