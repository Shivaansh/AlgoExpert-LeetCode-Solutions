# Import time module
import time
####################### START CODE TO CHECK RUNTIME FOR ##################################    
def longestSubstringWithoutDuplication1(string):
    # Write your code here.
    charset = set()

    maxSubstringLength = float('-inf')
    maxSubstring = ""
    start = 0
    current = start
    currentLength = 0

    while(current < len(string)):
        if(string[current] not in charset):
            charset.add(string[current])
            currentLength += 1
            current += 1
        else:
            if(currentLength > maxSubstringLength):
                maxSubstringLength = currentLength
                maxSubstring = string[start:current]
            currentLength = 0
            start += 1
            current = start
            charset = set()

    if(currentLength > maxSubstringLength):
        maxSubstring = string[start:current]
        
    return maxSubstring

def longestSubstringWithoutDuplication2(string):
    # Write your code here.
    charTable = {}

    maxSubstringLength = float('-inf')
    maxSubstring = ""
    start = 0
    current = start
    currentLength = 0

    while(current < len(string)):
        if(string[current] not in charTable):
            charTable[string[current]] = current
            currentLength += 1
            current += 1
        else:
            if(currentLength > maxSubstringLength):
                maxSubstringLength = currentLength
                maxSubstring = string[start:current]
            start = charTable[string[current]]+1
            currentLength = current-start
            charTable.clear()
            for i in range(start, current):
                if(string[i] not in charTable):
                    charTable[string[i]] = i

    if(currentLength > maxSubstringLength):
        maxSubstring = string[start:current]
        
    return maxSubstring

####################### END CODE TO CHECK RUNTIME FOR ##################################    
# record start time
start = time.time()
 
# Copy code to check runtime for
print(longestSubstringWithoutDuplication1("abacacacaaabacaaaeaaafa"))
# Mark end time of code
end = time.time()
 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program 1 is :",
      (end-start) * 10**3, "ms")

start = time.time()
 
# Copy code to check runtime for
print(longestSubstringWithoutDuplication2("abacacacaaabacaaaeaaafa"))
# Mark end time of code
end = time.time()
 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program 2 is :",
      (end-start) * 10**3, "ms")
