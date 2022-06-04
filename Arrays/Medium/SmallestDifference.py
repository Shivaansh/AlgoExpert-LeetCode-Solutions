def smallestDifference(arrayOne, arrayTwo):
    #Name: Smallest Difference
	#Category and difficulty: Arrays, Medium
    #time: O(m + n) since we run through both the arrays once
	#space: O(1)

    arrayOne.sort()
    arrayTwo.sort()

    number1 = -1
    number2 = -1
    p1 = 0
    p2 = 0
    minDiff = 9999999999
    
    while(p1 < len(arrayOne) and p2 < len(arrayTwo)):
        currentDiff = abs(arrayOne[p1] - arrayTwo[p2])
        if(currentDiff < minDiff):
            minDiff = currentDiff
            number1 = p1
            number2 = p2
        if(currentDiff == 0):
            return [arrayOne[p1], arrayTwo[p2]]
            
        if(arrayOne[p1] < arrayTwo[p2]):
            p1 += 1
        elif(arrayOne[p1] > arrayTwo[p2]):
            p2 += 1

    return [arrayOne[number1], arrayTwo[number2]]
        
    pass