def sortedSquaredArray(array):
    #Name: Sorted Squared Array
	#Category and difficulty: Arrays, Easy
    #time: O(n)
	#space: O(n)
	
	newArray = []
	maxPos = 0 #index of max number in squared array
	minPos = 0 #index of min number in squared array
	
	newArray.append(array[0]**2) #add first number to array to initialize
	
	#add squared numbers to array and move to correct position, adjust min and max indices
	for i in range(1, len(array)):
		newNum = array[i]**2
		if(newNum >= newArray[maxPos]):
			newArray.append(newNum)
			maxPos = len(newArray) - 1
		elif(newNum <= newArray[minPos]):
			newArray.insert(0, newNum)
			minPos = 0
			maxPos = len(newArray) - 1
		else:
			ind = minPos
			while(newArray[ind] < newNum):
				ind += 1
			newArray.insert(ind, newNum)
			maxPos = len(newArray) - 1
    return newArray