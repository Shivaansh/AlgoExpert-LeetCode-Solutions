def longestSubstringWithoutDuplication(string):
    #Name: Longest Substring Without Duplication
	#Category and difficulty: Strings, Hard
    #time: O(n) at max since we go through the string through a window
	#space: Max O(n) where n is the number of UNIQUE characters in the string 
    
    charTable = {}

    maxSubstringLength = float('-inf')
    maxSubstring = ""
    start = 0
    current = start
    currentLength = 0

    while(current < len(string)):
        if(string[current] not in charTable):
            charTable[string[current]] = current
            currentLength += 1
            current += 1
        else:
            if(currentLength > maxSubstringLength):
                maxSubstringLength = currentLength
                maxSubstring = string[start:current]
            start = charTable[string[current]]+1
            currentLength = current-start
            charTable.clear()
            for i in range(start, current):
                if(string[i] not in charTable):
                    charTable[string[i]] = i

    if(currentLength > maxSubstringLength):
        maxSubstring = string[start:current]
        
    return maxSubstring