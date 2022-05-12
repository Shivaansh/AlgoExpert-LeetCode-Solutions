def firstNonRepeatingCharacter(string):
    #Name: First Non-Repeating Character
	#Category and difficulty: Strings, Easy
    #time: O(n) - one interation of string
	#space: O(1) - can have a maximum of 26 entries in the hash table
	
	countsTable = {} #Hash Table to count instances of each character
	minIndex = 10000000000000 #initialize minIndex to keep track of lowest index of non-repeating character
	
	#populate hash table with counts of each character
	for i in string:
		if(not (i in countsTable)):
			countsTable[i] = 0
		countsTable[i] += 1
		
	#retrieve list of non-repeating characters
	nonRepeatingChars = [k for k, v in countsTable.items() if v == 1]
	
	#edge case
	if(len(nonRepeatingChars) == 0):
		return -1
	
	#check index of each non repeating character and record the lowest index
	for i in nonRepeatingChars:
		if(minIndex > string.index(i)):
			minIndex = string.index(i)
	return minIndex