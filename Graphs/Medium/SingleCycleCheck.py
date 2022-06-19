def hasSingleCycle(array):
    #Name: Single Cycle Check
	#Category and difficulty: Graphs, Medium
    #time: O(n), where n is the length of the array
	#space: O(1)
    index = 0
    length = len(array)
    count = 0
    mark = -123123123123123
    startMark = -999999

    #Only continue while not repeating elements in array
    while(count < length):
        #When a zero is encountered, we will never move anywhere
        if(array[index] == 0):
            return False
        #If reached starting number before going through entire array, more than one cycle
        if(array[index] == startMark and count < length):
            return False
        
        count += 1
        sum = index + array[index]

        #Mark number as simply visited or starting index
        if(index == 0):
            array[index] = startMark
        else:
            array[index] = mark

        #Increase index 
        if(sum < 0 or sum >= length):
            index = sum % length
        else:
            index = sum

        #Check if cycling in array
        if(count > length+1 or array[index] == mark):
            return False
            
    return True
    pass