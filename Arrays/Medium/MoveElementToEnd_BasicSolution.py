def moveElementToEnd(array, toMove):
    #Name: Move Element to End
	#Category and difficulty: Arrays, Medium
    #time: O(n ^ 2) since we do an O(n) operation (worst case) for every element of the array
	#space: O(n) since push and pop are not in-place operations in python

    #O(n)
    count = 0
    for num in array:
        if(num == toMove):
            count += 1

    #O(n ^ 2)
    index = 0
    while(index < len(array)):
        if(array[index] == toMove and (not arrayIsArrangedProperly(array, count, toMove))):
            array.pop(index)
            array.append(toMove)
        else:
            index += 1
    return array
    pass

#O(n) in the worst case
def arrayIsArrangedProperly(arr, instances, target):
    for index in range((len(arr) - instances), len(arr)):
        if(arr[index] != target):
            return False
    return True
