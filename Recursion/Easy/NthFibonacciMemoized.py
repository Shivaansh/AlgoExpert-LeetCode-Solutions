def getNthFib(n, resultsStore = {0 : 0, 1 : 0, 2 : 1}):
    #Name: Nth Fibonacci
	#Category and difficulty: Recursion, Easy
    #time: O(n)
	#space: O(n)

	if(n in resultsStore):
		return resultsStore[n]
	else:
		resultsStore[n] = getNthFib(n - 1) + getNthFib(n - 2)
		return resultsStore[n]	
    pass
