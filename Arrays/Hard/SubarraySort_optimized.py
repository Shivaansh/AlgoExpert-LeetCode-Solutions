def subarraySort(array):
    #Name: Subarray Sort
	#Category and difficulty: Arrays, Hard
    #time: O(n)
	#space: O(1)
    start = -1
    end = -1

    smallestOutOfOrder = float('inf')
    largestOutOfOrder = float('-inf')
    
    #Handle edge case of array size 2 AND if entire array needs to be sorted, can check only first and last elements
    if(array[0] > array[1]):
        start = 0
    if(array[len(array)-1] < array[len(array)-2]):
        end = len(array)-1
    if(start != -1 and end != -1):
        return [start, end]
        
    
    for ind in range(1, len(array)-1):
        current = array[ind]
        prev = array[ind-1]
        succ = array[ind+1]
        if(checkOutOfOrder(current, prev, succ)):
            if(smallestOutOfOrder > current):
                smallestOutOfOrder = current
            if(largestOutOfOrder < current):
                largestOutOfOrder = current

    if(array[0] > array[1]):
        if(array[0] < smallestOutOfOrder):
            smallestOutOfOrder = array[0]
        elif(array[0] > largestOutOfOrder):
            largestOutOfOrder = array[0]
    if(array[len(array)-1] < array[len(array)-2]):
        if(array[len(array)-1] < smallestOutOfOrder):
            smallestOutOfOrder = array[len(array)-1]
        elif(array[len(array)-1] > largestOutOfOrder):
            largestOutOfOrder = array[len(array)-1]
    
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

def checkOutOfOrder(number, prev, succ):
    
    return (number < prev or number > succ)