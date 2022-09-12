def subarraySort(array):
    #Name: Subarray Sort
	#Category and difficulty: Arrays, Hard
    #time: O(n)
	#space: O(1)
    start = -1
    end = -1

    smallestOutOfOrder = float('inf')
    largestOutOfOrder = float('-inf')
    
    for ind in range(len(array)):
        current = array[ind]
        if(checkOutOfOrder(current, ind, array)):
            if(smallestOutOfOrder > current):
                smallestOutOfOrder = current
            if(largestOutOfOrder < current):
                largestOutOfOrder = current
    
    #find correct position for smallestOutOfOrder
    for i in range(len(array)):
        if(array[i] > smallestOutOfOrder):
            start = i
            break

    for i in reversed(range(len(array))):
        if(array[i] < largestOutOfOrder):
            end = i
            break
    return [start, end]

def checkOutOfOrder(number, index, array):
    if(index == 0):
        return (number > array[index+1])
    elif(index == len(array)-1):
        return (number < array[index-1])
    return (number < array[index-1] or number > array[index+1])