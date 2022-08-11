def minNumberOfCoinsForChange(n, denoms):
    #Name: Min Number of Coins For Change
	#Category and difficulty: Dymamic Programming, Medium
    #time: O(n * d) where n is the given number and d is the number of denominations of coins
	#space: O(n)

    #Edge case
    if(n <= 0):
        return 0
    #Initialize store of results for values from 0 to n
    minCoins = [999999]*(n+1)
    minCoins[0] = 0
    
    for den in denoms:
        for num in range(1, n+1):
            #Check number of coins needed
            if(num - den >= 0):
                count = 1 + minCoins[num-den]
            else:
                count = 0 
            #Update min coin count         
            if(count != 0 and count < minCoins[num]):
                    minCoins[num] = count  
    #Return min count coint if updated
    if(minCoins[-1] != 999999):
        return minCoins[-1]
    return -1
