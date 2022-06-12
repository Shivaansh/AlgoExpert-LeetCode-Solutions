def reverseWordsInString(string):
    #Name: Reverse words in string
	#Category and difficulty: Strings, Medium
    #time: O(n): We go through the input string once
	#space: O(n) since we return a string of same length
    
    returnString = ""
    tempString = ""

    for char in reversed(range(len(string))):
        if(string[char] != ' '):
            tempString += string[char]
        else:
            if(tempString != ""):
                returnString += reverseAString(tempString)
                tempString = ""
            returnString += " "
    if(tempString != ""):
        returnString += reverseAString(tempString)
    print(returnString)
    
    return returnString

def reverseAString(string):
    newString = ""
    for i in reversed(range(len(string))):
        newString += string[i]
    return newString
        
