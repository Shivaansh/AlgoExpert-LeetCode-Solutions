def findThreeLargestNumbers(array):
    #Name: Find three largest numbers
	#Category and difficulty: Searching, Easy
    #time: O(n) if array is unsorted, O(log n) if sorted
	#space: O(1)

	ansList = []
	firstMax = -99999999
	secondMax = -99999999
	thirdMax = -99999999
	
	#first pass
	for i in range(len(array)):
		if (array[i] > firstMax):
			firstMax = array[i]
			firstMaxIndex = i
	
	#second pass
	for j in range(len(array)):
		if (array[j] > secondMax and j != firstMaxIndex):
			secondMax = array[j]
			secondMaxIndex = j
			
	#third pass
	for k in range(len(array)):
		if (array[k] > thirdMax and k != firstMaxIndex and k != secondMaxIndex):
			thirdMax = array[k]
	
	#add first element to list
	ansList.append(firstMax)
	
	#add second element to list in correct place
	if(secondMax >= firstMax):
		ansList.append(secondMax)	
	else:
		ansList.insert(0, secondMax)
		
	lo = 0
	hi = 1
	
	
	#add third element to list in correct place
	if(thirdMax <= ansList[lo]):
		ansList.insert(0, thirdMax)
	elif(thirdMax <= ansList[hi] and thirdMax >= ansList[lo]):
		ansList.insert(1, thirdMax)
	else:
		ansList.append(thirdMax)
	
	return ansList
    pass