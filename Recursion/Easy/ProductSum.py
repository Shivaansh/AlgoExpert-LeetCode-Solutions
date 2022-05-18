def productSum(array):
    #Name: Product Sum
	#Category and difficulty: Recursion, Easy
    #time: O(n) - going through array once
	#space: O(nm) - m is MAX DEPTH of array

	depth = 1
	return getProductSum(array, depth)
    pass

def getProductSum(arr, dpth):
	arrSum = 0
	for element in arr:
		if type(element) is list:
			arrSum += getProductSum(element, dpth+1)
		else:
			arrSum += element
	return (dpth * arrSum)