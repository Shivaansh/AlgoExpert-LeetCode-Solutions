def numberOfWaysToMakeChange(n, denoms):
    #Name: Number of ways to make change
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(n * d) where n is the given number and d is the number of denominations of coins
	#space: O(n)
    
    #Edge cases
    if(n == 0):
        return 1
    if(len(denoms) == 0):
        return 0

    #Store results of ways from 0 to n
    nWays = [0]*(n+1)
    nWays[0] = 1

    #Denoms length = d
    for denom in denoms:
        #nums length = n
        for i in range(n+1):
            #Safety for index out of bounds error
            if(i-denom >= 0):
                nWays[i] += nWays[i-denom]
    return nWays[-1]
