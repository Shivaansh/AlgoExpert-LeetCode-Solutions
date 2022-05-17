def firstNonRepeatingCharacter(string):
    #Name: First Non-Repeating Character
	#Category and difficulty: Strings, Easy
    #time: O(n) - one interation of string
	#space: O(1) - can have a maximum of 26 entries in the hash table
	
	countsTable = {} #Hash Table to count instances of each character
	
	#populate hash table with counts of each character
	for i in string:
		if(not (i in countsTable)):
			countsTable[i] = 0
		countsTable[i] += 1
	
	#check frequency of each character and return the first index
	for i in range(len(string)):
		char = string[i]
		if(countsTable[char] == 1):
			return i
	return -1
