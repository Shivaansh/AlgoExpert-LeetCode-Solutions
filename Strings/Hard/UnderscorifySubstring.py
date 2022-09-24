def underscorifySubstring(string, substring):
    #Name: Underscorify Substring
	#Category and difficulty: Strings, Hard
    #time: O(n/k) ~ O(n) where k is size of substring
	#space: Max O(n) where n is the length of string

    #Edge case
    if(substring == ""):
        return "_" + string + "_"
        
    ssLength = len(substring)
    current = 0

    while(current < len(string)):
        #CASE - substring found
        if(string[current:current+ssLength] == substring):
            start = current
            end = findend(string, substring, start)
            string = string[:start] + "_" + string[start:end] + "_" + string[end:]
            current = end+1
        #CASE - substring not found
        else:
            current += 1
            
    return string

def findend(string, substring, startPoint):
    ssLength = len(substring)
    endPoint = startPoint + ssLength

    #This is also an edge case
    if(ssLength == 1):
        current = startPoint+1
        while(current < len(string) and string[current] == substring[0]):
            current += 1
        return current
        
    anchor = startPoint+1
    current = anchor
    while(endPoint < len(string) and current <= endPoint):
        if(string[current : current + ssLength] == substring):
            endPoint = current + ssLength
        current += 1
    return endPoint
