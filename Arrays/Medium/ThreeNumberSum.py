def threeNumberSum(array, targetSum):
    #Name: Three Number Sum
	#Category and difficulty: Arrays, Medium
    #time: O(n^2) since we run through the array once for every element of the array
	#space: O(n) - Output array is similar to size of input array, 
    array2d = []
    array.sort()

    #range is length - 2 to accomodate for lo and hi indices
    for i in range(len(array)-2):
        number = array[i]
        tempTarget = targetSum - number
        lo = i + 1
        hi = len(array)-1
        answerArray = [number]

        #avoiding calculation using current number due to distinct property of triplets
        if(array[lo] == number):
            lo += 1
        if(array[hi] == number):
            hi -= 1 

        #performing Two Sum operation for tempTarget
        while(lo < hi):
            if(array[lo] + array[hi] == tempTarget):
                answerArray.append(array[lo])
                answerArray.append(array[hi])
                answerArray.sort()
                if(answerArray not in array2d):
                    array2d.append(answerArray)
                    #resetting answerArray coz multiple doublets possible for number
                    answerArray = [number]
                    lo += 1
                    hi -= 1
            elif(array[lo] + array[hi] < tempTarget):
                lo += 1
            else:
                hi -= 1
                
    return array2d      
    pass
