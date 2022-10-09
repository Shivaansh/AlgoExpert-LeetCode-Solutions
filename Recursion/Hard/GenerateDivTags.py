def generateDivTags(numberOfTags):
    #Name: Generate Div Tags
    #Category and difficulty: Recursion, Hard
    #time: O(4^n * n)
    #space: O(4^n * m + m) for storing all strings and space used by checkIfValid function
    allPatterns = generateDivTagsHelper(numberOfTags)
    validPatterns = []
    #O(4^n * n) time, O(4^n * m + m) space where m is the length of a string combination for number n
    for pattern in allPatterns:
        if(checkIfValid(pattern) == True):
            validPatterns.append(''.join(pattern))
    return validPatterns
    
#O(4^n) time, O(4^n * m) space where m is the length of a string combination for number n
#A set of open and close tags is 11 characters long, so m = n * 11 characters
def generateDivTagsHelper(number):
    #Edge case
    if(number == 1):
        return [["<div>", "<div>"], ["<div>", "</div>"], ["</div>", "<div>"], ["</div>", "</div>"]]
    
    #Create all possible string combinations
    listOfTags = []
    innerTags = generateDivTagsHelper(number-1)
    
    for combination in innerTags:
        current = ["<div>"] + combination + ["</div>"] 
        listOfTags.append(current)
        
        current = ["<div>"] + combination + ["<div>"] 
        listOfTags.append(current)
        
        current = ["</div>"] + combination + ["</div>"] 
        listOfTags.append(current)
        
        current = ["</div>"] + combination + ["<div>"] 
        listOfTags.append(current)
        
    return listOfTags
    
#O(n) time and space where n is the length of the pattern
def checkIfValid(pattern):
    stack = []
    for element in pattern:
        if(element == "<div>"):
            stack.append(element)
        elif(element == "</div>"):
            if(len(stack) > 0 and stack[-1] == "<div>"):
                stack.pop()
            else:
                return False
    if(len(stack) == 0):
        return True
    return False
        
