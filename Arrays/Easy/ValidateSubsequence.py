def isValidSubsequence(array, sequence):
    #Name: Validate Subsequence
	#Category and difficulty: Arrays, Easy
    #time: O(n)
	#space: O(1)
	
	#edge case
	if(len(sequence) == 0): 
		return False
	sInd = 0 #subsequence index
	mInd = 0 #main array index
	#Check order of numbers in main and subsequence arrays
	while(sInd < len(sequence)):
		if(mInd < len(array) and array[mInd] == sequence[sInd]):
			mInd += 1
			sInd += 1
		elif(mInd == len(array)):
			return False
		else:
			mInd += 1
	return True
    pass
