def getNthFib(n):
    #Name: Nth Fibonacci
	#Category and difficulty: Recursion, Easy
    #time: O(n)
	#space: O(1)

	if(n <= 1):
		return 0
	if(n == 2):
		return 1
	
	return getNthFib(n - 1) + getNthFib(n - 2)
	
    pass
