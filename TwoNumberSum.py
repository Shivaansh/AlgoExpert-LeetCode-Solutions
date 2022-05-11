def twoNumberSum(array, targetSum):
    #Name: Two Number Sum
	#Category and difficulty: Arrays, Easy
    #time: O(n)
	#space: O(n)
	#edge case
	if(len(array) < 2):
		return []
	#create and populate hashset
	hashset = set([])
	for i in array:
		hashset.add(i)
	#look for sum keeping conditions in check
	for i in array:
		if((targetSum - i) in hashset and (targetSum - i) != i):
			return [i, (targetSum - i)]
	return []
    pass