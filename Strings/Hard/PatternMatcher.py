def patternMatcher(pattern, string):
    #Name: Pattern Matcher
	#Category and difficulty: Strings, Hard
    #time: O(n^2 + m) where n is length of string and m is length of pattern
	#space: (n + m)

    ##DISCLAIMER: This code has been written by me on the basis of the concepual Walkthrough provided on AlgoExpert.io video solutions for this problem
    
    stringStartsWithY = startsWithY(pattern)
    patternArray = getPattern(pattern)
    frequencies = getFrequencies(patternArray)
    xCount = frequencies['x']
    yCount = frequencies['y']
    firstYIndex = firstYPosition(patternArray)

    if(yCount == 0):
        xLen = len(string)/xCount
        xString = string[0:int(xLen)]
        ans = [xString, ""]
        if(stringStartsWithY):
            ans.reverse()
        return ans

    for n in range(1, len(string)):
        newPatternArray = []
        xLength = int(n)
        yLength = (len(string) - (xLength * xCount)) / yCount
        yStartIndex = (xLength * firstYIndex)
        yEndIndex = yStartIndex + int(yLength)
        xSubstring = string[0:xLength]
        ySubstring = string[yStartIndex:yEndIndex]

        for char in patternArray:
            if(char == 'x'):
                newPatternArray.append(xSubstring)
            else:
                newPatternArray.append(ySubstring)
        newPattern = ''.join(newPatternArray)
        
        if(newPattern == string):
            ans = [xSubstring, ySubstring]
            if(stringStartsWithY):
                ans.reverse()
            return ans
            
    return []
        
###################################### HELPER FUNCTIONS ########################################

def startsWithY(pattern):
    return pattern[0] == 'y'

def getPattern(pattern):
    arr = []
    for ind in range(len(pattern)):
        arr.append(pattern[ind])

    if(startsWithY(pattern)):
        #Swap x and y characters in pattern
        for ind in range(len(arr)):
            if(arr[ind] == 'x'):
                arr[ind] = 'y'
            elif(arr[ind] == 'y'):
                arr[ind] = 'x'
    return arr

def getFrequencies(list):
    counts = {'x' : 0, 'y' : 0}
    for char in list:
        counts[char] += 1
    return counts

def firstYPosition(list):
    for ind in range(len(list)):
        if(list[ind] == 'y'):
            return ind
    return -1