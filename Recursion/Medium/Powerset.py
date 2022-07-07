def powerset(array):
    #Name: Powerset
	#Category and difficulty: Recursion, Medium
    #time: O(n * 2^n)
	#space: O(n * 2^n)
    powerSets = []
    getPowerSetsHelper(array, powerSets)
    return powerSets

def getPowerSetsHelper(array, powerSets):
    #There are 2^n powersets for an array of n elements
    if(array not in powerSets):
        powerSets.append(array)
    #Runs n times for length of array
    if(len(array) > 0):
        for index in range(len(array)):
            subArray = array[:index] + array[index+1:]
            getPowerSetsHelper(subArray, powerSets)
