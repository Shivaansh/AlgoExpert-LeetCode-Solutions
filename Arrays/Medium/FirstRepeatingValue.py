def firstDuplicateValue(array):
    #Name: Monotonic Array
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we run through the array once
	#space: O(n) since the hashset can have max size in the order of O(n)
    hashset = set()
    for val in array:
        if(val in hashset):
            return val
        hashset.add(val)
    return -1
    #Note: This is the most optimal solution I came up with, but AlgoExpert has a more optimal solution that I shall not share due to copyright reasons.