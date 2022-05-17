def generateDocument(characters, document):
    #Name: Generate Document
	#Category and difficulty: Strings, Easy

    ## Approach 1: O(m+n) time and space
    #time: O(m+n)
	#space: O(m+n)
	if(document == ""):
		return True
	if(characters == ""):
		return False
	
	charSet = {}
	docSet = {}
	
	for i in characters:
		if(i not in charSet):
			charSet[i] = 0
		charSet[i] += 1
	
	for i in document:
		if(i not in docSet):
			docSet[i] = 0
		docSet[i] += 1
	
	for i in docSet.keys():
		if(i not in charSet or docSet[i] > charSet[i]):
			return False
    return True


def generateDocument(characters, document):
    ## Approach 2: O(n) space
    #time: O(m+n)
	#space: O(n)
	if(document == ""):
		return True
	if(characters == ""):
		return False
	
	charSet = {}
	
	for i in characters:
		if(i not in charSet):
			charSet[i] = 0
		charSet[i] += 1
	
	for i in document:
		if(i not in charSet or charSet[i] == 0):
			return False
		charSet[i] -= 1
    return True
