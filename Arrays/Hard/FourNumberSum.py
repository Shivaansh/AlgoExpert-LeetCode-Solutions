def fourNumberSum(array, targetSum):
    #Name: Four Number Sum
	#Category and difficulty: Arrays, Hard
    #time: O(n^2) - O(n^3) in average-worst case
	#space: O(n^2) for size of hashmap
    quads = []
    pairMap = {}

    for n1Index in range(1, len(array)-1):
        num1 = array[n1Index]
        #forward operations - update quadruplets
        for n2Index in range(n1Index+1, len(array)):
            num2 = array[n2Index]
            diff = targetSum - (num1 + num2)
            if(diff in pairMap):
                for pair in pairMap[diff]:
                    quads.append(pair + [num1, num2])
        #reverse operations - populate hashmap
        for n3Index in reversed(range(n1Index)):
            num3 = array[n3Index]
            if((num1 + num3) not in pairMap):
                pairMap[num1 + num3] = [[num1, num3]]
            else:
                pairMap[num1 + num3].append([num1, num3])

    return quads