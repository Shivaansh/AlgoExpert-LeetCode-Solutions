def isPalindrome(string):
    #Name: Palindrome Check
	#Category and difficulty: Strings, Easy
    #time: O(n)
	#space: O(1)
	leftPointer = 0
	rightPointer = len(string)-1
	
	while(leftPointer < rightPointer):
		if(string[leftPointer] != string[rightPointer]):
			return False
		leftPointer += 1
		rightPointer -= 1
	return True
    pass