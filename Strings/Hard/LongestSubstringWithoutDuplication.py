def longestSubstringWithoutDuplication(string):
    #Name: Longest Substring Without Duplication
	#Category and difficulty: Strings, Hard
    #time: O(n) at max since we go through the string through a window
	#space: Max O(n) where n is the number of UNIQUE characters in the string 
    charTable = {}
    maxSubstring = ""
    startIdx = 0
    current = 0

    while(current < len(string)):
        if(string[current] not in charTable):
            charTable[string[current]] = current
        else:
            startIdx = max(startIdx, charTable[string[current]]+1)
        currentSubstring = string[startIdx:current+1]
        if(len(currentSubstring) > len(maxSubstring)):
            maxSubstring = currentSubstring
        charTable[string[current]] = current
        current += 1

    if(len(currentSubstring) > len(maxSubstring)):
        maxSubstring = currentSubstring
        
    return maxSubstring
