def nonConstructibleChange(coins):
    #Name: Non Constructible Change
	#Category and difficulty: Arrays, Easy
    #time: O(n)
	#space: O(1)
	
	coins.sort() #sorting array made it easier to find patterns
	currChange = 0
	for i in coins:
		if (i > currChange + 1): #this relation was observed via sample cases
			return currChange + 1
		currChange += i
	return currChange + 1
