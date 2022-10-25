def arrayOfProducts(array):
    #Name: Array of Products
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we run through the array exactly two times
	#space: O(n) sinze we create an extra array of size n
    leftProduct = 1
    answerArray = [1] * len(array)
    rightProduct = 1
    
    for i in range(len(array)):
        answerArray[i] = leftProduct
        leftProduct *= array[i]

    for i in reversed(range(len(array))):
        answerArray[i] *= rightProduct
        rightProduct *= array[i]
        
    return answerArray
