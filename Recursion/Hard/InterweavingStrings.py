def interweavingStrings(one, two, three):
    #Name: Interweaving Strings
    #Category and difficulty: Recursion, Hard
    #time: O(m + n) where m and n are lengths of one and two
    #space: O(1)
    if(len(three) < len(one) + len(two)):
        return False

    endOfOne = len(one)
    endOfTwo = len(two)
    endOfThree = len(three)

    oneIndex = 0
    twoIndex = 0
    threeIndex = 0

    while(threeIndex < endOfThree and oneIndex <= endOfOne and twoIndex <= endOfTwo):
        #if both strings have the same character, decide how to proceed
        if(oneIndex < endOfOne and twoIndex < endOfTwo and one[oneIndex] == three[threeIndex] and two[twoIndex] == three[threeIndex]):
            nextOne = oneIndex + 1
            nextTwo = twoIndex + 1
            nextThree = threeIndex + 1
            if(nextThree < endOfThree and nextTwo < endOfTwo and three[nextThree] == two[nextTwo]):
                twoIndex += 1
            else:
                oneIndex += 1
        elif(oneIndex < endOfOne and one[oneIndex] == three[threeIndex]):
            oneIndex += 1
        elif(twoIndex < endOfTwo and two[twoIndex] == three[threeIndex]):
            twoIndex += 1
        else:
            return False
        threeIndex += 1
            
    return (threeIndex == endOfThree and oneIndex == endOfOne and twoIndex == endOfTwo)
