def generateDivTags(numberOfTags):
    #Name: Generate Div Tags
    #Category and difficulty: Recursion, Hard
    #time: O((2n)!/(n!(n+1)!))
    #space: O((2n)!/(n!(n+1)!))
    currentString = ""
    listOfTags = []
    generateDivTagsHelper(numberOfTags, numberOfTags, currentString, listOfTags)
    return listOfTags

def generateDivTagsHelper(nOpening, nClosing, currentString, listOfStrings):
    if(nOpening == 0 and nClosing == 0):
        listOfStrings.append(currentString)
        return 
    if(nOpening == 0 and nClosing > 0):
        for i in range(nClosing):
            currentString = currentString + "</div>"
        listOfStrings.append(currentString)
        return
        
    if(nOpening == nClosing):
        newString = currentString + "<div>" 
        generateDivTagsHelper(nOpening-1, nClosing, newString, listOfStrings)
    elif(nOpening < nClosing):
        newString1 = currentString + "<div>"
        generateDivTagsHelper(nOpening-1, nClosing, newString1, listOfStrings)
        newString2 = currentString + "</div>"
        generateDivTagsHelper(nOpening, nClosing-1, newString2, listOfStrings)