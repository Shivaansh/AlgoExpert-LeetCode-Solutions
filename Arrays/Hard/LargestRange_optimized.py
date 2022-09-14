def largestRange(array):
    #Name: Largest Range
	#Category and difficulty: Arrays, Hard
    #time: O(n)
	#space: O(n)

    #O(n) space and time
    hashTable = {}
    for num in array:
        #set all numbers to not visited yet
        hashTable[num] = False

    #O(n) time
    maxLength = -1
    currLength = 0
    maxRange = [-1, -1]
    for num in array:
        if(hashTable[num]):
            continue
        #set num to visited
        hashTable[num] = True
        currLength = 1
        left = num-1
        right = num+1
        while(left in hashTable):
            currLength += 1
            hashTable[left] = True
            left -= 1
        while(right in hashTable):
            currLength += 1
            hashTable[right] = True
            right += 1
        if(currLength > maxLength):
            maxLength = currLength
            maxRange = [left+1, right-1]

    return maxRange
