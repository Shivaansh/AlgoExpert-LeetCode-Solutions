def minNumberOfJumps(array):
    #Name: Min Number of Jumps
	#Category and difficulty: Dymamic Programming, Hard
    #time: O(n) for 1 pass of array
	#space: O(1)
    
    # Explore all positions you can reach from all the options available to you, 
    # then jump to the max position discovered
    if(len(array) <= 1):
        return 0
    jumps = 0
    maxPossibleIndexReached = array[0]
    steps = array[0]
    for index in range(1, len(array)):
        if(index == len(array)-1):
            return jumps+1
        maxPossibleIndexReached = max(maxPossibleIndexReached, index+array[index])
        steps -= 1
        if(steps == 0):
            jumps += 1
            steps = maxPossibleIndexReached - index
