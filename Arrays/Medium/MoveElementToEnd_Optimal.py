def moveElementToEnd(array, toMove):
    #Name: Move Element to End
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we run through the array once
	#space: O(1) since we only use two pointers
    i = 0
    j = len(array) - 1

    while(i < j):
        while(i < j and array[j] == toMove):
            j -= 1
        if(i < j and array[i] == toMove):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        i += 1

    return array
    pass
