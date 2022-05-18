def binarySearch(array, target):
    #Name: Binary Search
	#Category and difficulty: Recursion, Easy
    #time: O(n log n) if array is unsorted, O(log n) if sorted
	#space: O(1)

	newArray = array
	newArray.sort()
	lo = 0
	hi = len(array)-1
	while(lo < hi):
		mid = int((lo + hi)/2)
		if(newArray[mid] == target):
			return mid
		elif(newArray[mid] < target):
			lo = mid + 1
		else:
			hi = mid
	
	if(newArray[lo] == target):
		return lo
	else:
		return -1
    pass
