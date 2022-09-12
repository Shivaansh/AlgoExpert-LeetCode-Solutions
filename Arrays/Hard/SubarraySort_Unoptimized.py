def subarraySort(array):
    #Name: Subarray Sort
	#Category and difficulty: Arrays, Hard
    #time: O(n log n)
	#space: O(n)
    array2 = sorted(array)
    i = 0
    j = len(array)-1
    start = -1
    end = -1
    while(i <= j):
        if(start == -1):
            if(array[i] != array2[i]):
                start = i
            else:
                i += 1
        if(end == -1):
            if(array[j] != array2[j]):
                end = j
            else:
                j -= 1
        if(start != -1 and end != -1):
            break

    return [start, end]
            
    pass
