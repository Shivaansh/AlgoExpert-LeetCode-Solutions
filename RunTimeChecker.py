# Import time module
import time
####################### START CODE TO CHECK RUNTIME FOR ##################################    
def largestRange1(array):
    # Write your code here.
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
    
    #O(m) time where m is max num in array
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

def largestRange2(array):
    # Write your code here.

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

####################### END CODE TO CHECK RUNTIME FOR ##################################    
# record start time
start = time.time()
 
# Copy code to check runtime for
print(largestRange1([1,2,3, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007]))
# Mark end time of code
end = time.time()
 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program 1 is :",
      (end-start) * 10**3, "ms")

start = time.time()
 
# Copy code to check runtime for
print(largestRange2([1,2,3, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007]))
# Mark end time of code
end = time.time()
 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program 2 is :",
      (end-start) * 10**3, "ms")
