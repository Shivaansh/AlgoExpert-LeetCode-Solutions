def longestPeak(array):
    #Name: Longest Peak
	#Category and difficulty: Arrays, Medium
    #time: O(n) since we run through the array once
	#space: O(1)

    #edge case, peak needs at least 3 numbers
    if(len(array) <= 2):
        return 0
        
    maxLengthOfPeak = 0
    index = 0
    
    #Range of loop chosen because peak requires one number on left and one number on right
    for index in range(1, len(array)-1):
        #Check if current number is peak
        if(array[index] > array[index-1] and array[index+1] < array[index]):
            startOfPeak = index-1
            endOfPeak = index+1

            #find length of strictly increasing array to left of peak
            while(startOfPeak > 0 and array[startOfPeak-1] < array[startOfPeak]):
                startOfPeak -= 1
            #find length of strictly decreasing array to right of peak
            while(endOfPeak < len(array)-1 and array[endOfPeak+1] < array[endOfPeak]):
                endOfPeak += 1
                
            #length of peak
            length = (endOfPeak - startOfPeak + 1)
            if(length > maxLengthOfPeak):
                maxLengthOfPeak = length
                
    return maxLengthOfPeak
    pass
