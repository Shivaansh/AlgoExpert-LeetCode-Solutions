def largestRange(array):
    #Name: Largest Range
	#Category and difficulty: Arrays, Hard
    #time: O(m) where m is the length of (arrayMax - arrayMin)
	#space: O(n)

    #O(n) space
    hashset = set(array)
    #O(n) time for both
    minNum = min(array)
    maxNum = max(array)

    num = minNum

    start = minNum
    end = -1
    currLength = 0
    maxLength = -1
    maxRange = [-1, -1]
    
    #O(m) time
    while(num <= maxNum):
        if(num in hashset):
            currLength += 1
            end = num
            num += 1
        else:
            if(currLength > maxLength):
                maxLength = currLength
                maxRange = [start, end]
            currLength = 0
            start = findNextStart(num, maxNum, hashset)
            num = start
        
    if(currLength > maxLength):
        maxLength = currLength
        maxRange = [start, end]

    return maxRange
    
#O(m) time at most
def findNextStart(num, limit, hashset):
    for i in range(num+1, limit+1):
        if(i in hashset):
            return i
    return limit+1
    
    pass
