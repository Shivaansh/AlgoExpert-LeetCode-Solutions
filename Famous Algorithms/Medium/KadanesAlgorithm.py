def kadanesAlgorithm(array):
    #Name: Kadane's Algorithm
	#Category and difficulty: Famous Algorithms, Medium
    #time: O(n)
	#space: O(1)
    globalMax = array[0]
    currentMax = globalMax
    for i in range(1, len(array)):
        currentMax = max(array[i], currentMax + array[i])
        if(currentMax > globalMax):
            globalMax = currentMax
    return globalMax