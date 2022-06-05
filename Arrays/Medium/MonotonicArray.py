def isMonotonic(array):
    #Name: Monotonic Array
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we run through the array once
	#space: O(1)
    if(len(array) <= 2):
        return True

    isDecreasing = False
    
    if(array[1] - array[0] < 0):
        isDecreasing = True
    elif(array[1] - array[0] == 0):
        number = array[0]
        index = 0
        while(array[index] == number):
            index += 1
            if(index == len(array)-1):
                return True
        if(array[index] - array[index-1] < 0):
            isDecreasing = True
        
    if(isDecreasing):
        for i in range(len(array)-1):
            if(array[i+1] - array[i] > 0):
                return False
    else:
        for i in range(len(array)-1):
            if(array[i+1] - array[i] < 0):
                return False
    return True
    pass
