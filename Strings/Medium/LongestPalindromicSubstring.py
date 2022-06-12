def longestPalindromicSubstring(string):
    #Name: Longest Palindromic Substring
	#Category and difficulty: Strings, Medium
    #time: O(n^3) since we run through the string once for each element of the string, then perform an O(n) operation for a matching element
	#space: O(n) since we return a string with max possible size n

    if(len(string) <= 1):
        return string
        
    longestPalindrome = ""
    longestLength = 0
    outerIndex = 0
    
    while(outerIndex < len(string)):
        shouldIncrement = True
        for ind in reversed(range(outerIndex, len(string))):
            if(string[outerIndex] == string[ind]):
                if(isPalindrome(string, outerIndex, ind) and (ind-outerIndex+1) > longestLength):
                    longestPalindrome = returnSubstring(string, outerIndex, ind)
                    longestLength = len(longestPalindrome)
                    outerIndex += 1
                    shouldIncrement = False
                    break
        if(shouldIncrement):
            outerIndex += 1

    return longestPalindrome
    pass

def isPalindrome(inString, start, end):
    i = start
    j = end
    while(i <= j):
        if(inString[i] != inString[j]):
            return False
        i += 1
        j -= 1
    return True

def returnSubstring(inString, start, end):
    rString = ""
    for i in range(start, end+1):
        rString += inString[i]
    return rString
