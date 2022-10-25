def minNumberOfJumps(array):
    #Name: Min Number of Jumps
	#Category and difficulty: Dymamic Programming, Hard
    #time: O(n^2) at max
	#space: O(n)
    if(len(array) <= 1):
        return 0
    #store min jumps needed for each index
    jumpsNeeded = [float('inf')] * len(array)
    jumpsNeeded[0] = 0
    
    for index in range(len(array)):
        currentJumps = jumpsNeeded[index]
        maxJumps = array[index]
        maxPossibleIndex = min(len(array), index+maxJumps+1)
        
        #Catch statement to prevent extra calculations when we can reach the last index
        if(maxPossibleIndex == len(array)):
            return currentJumps+1
        #Update minjumps needed for each index possible from current
        for newIndex in range(index, maxPossibleIndex):
            jumpsNeeded[newIndex] = min(jumpsNeeded[newIndex], currentJumps+1)
    return jumpsNeeded[-1]
