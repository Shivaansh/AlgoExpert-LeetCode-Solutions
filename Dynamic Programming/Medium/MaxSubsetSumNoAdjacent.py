def maxSubsetSumNoAdjacent(array):
    #Name: Max Subset Sum No Adjacent
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(n)
	#space: O(1)

    ## Disclaimer: While the code written here is my own creation, the logic / solution reflected in the code is as explained in the video solutions on AlgoExpert.io, for this problem

    #Edge cases
    if(len(array) == 0):
        return 0  
    elif(len(array) == 1):
        return array[0]

    valA = array[0]
    valB = max(array[0], array[1])
    for ind in range(2, len(array)):
        current = max(valB, valA + array[ind])
        valA = valB
        valB = current
    return valB

