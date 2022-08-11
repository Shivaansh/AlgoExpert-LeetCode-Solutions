def maxSubsetSumNoAdjacent(array):
    #Name: Max Subset Sum No Adjacent
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(n)
	#space: O(1)

    #Edge cases
    if(len(array) == 0):
        return 0
    elif(len(array) == 1):
        return array[0]

    sum1 = array[0]
    sum2 = max(sum1, array[1])

    for ind in range(2, len(array)):
        newSum = max(sum2, sum1+array[ind])
        sum1 = sum2
        sum2 = newSum
    return sum2

