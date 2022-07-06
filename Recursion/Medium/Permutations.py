def getPermutations(array):
    #Name: Permutations
	#Category and difficulty: Recursion, Medium
    #time: O(n * n!)
	#space: O(n * n!)

    #Array to return to 
    mainArray = []
    getPermutationsHelper(array, [], mainArray)
    return mainArray

#Recursively create new permutations and add to mainArray
def getPermutationsHelper(array, currPerm, mainArray):
    #Base case
    if((array is not None and len(array) == 0) and len(currPerm) > 0):
        mainArray.append(currPerm)  
    #Recursive step  
    else:
        #Creating permutations for CURRENT element in array
        for index in range(len(array)):
            newArray = array[:index] + array[index+1:]
            perm = currPerm + [array[index]]
            getPermutationsHelper(newArray, perm, mainArray)

