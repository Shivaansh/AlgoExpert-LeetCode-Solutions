def minimumCharactersForWords(words):
    #Name: Minimum Characters for Words
	#Category and difficulty: Strings, Medium
    #time: O(n * m): We go through n strings of max length m
	#space: O(k) where k is the number of unique characters in all the strings

    #Hash table to track frequencies of all characters
    mainHashTable = {}

    #iterate through each string
    for word in words:
        #Hash table to track frequencies of all characters in current string
        wordHashTable = {}
        for char in word:
            if(char not in wordHashTable):
                wordHashTable[char] = 1
            else:
                wordHashTable[char] += 1
        #Update mainHashTable with frequencies of characters in current string
        for key in wordHashTable:
            if((key not in mainHashTable) or (mainHashTable[key] < wordHashTable[key])):
                mainHashTable[key] = wordHashTable[key]
    
    returnArray = []
    #populate return array with characters
    for key, value in mainHashTable.items():
        for i in range(value):
            returnArray.append(str(key))

    return returnArray
