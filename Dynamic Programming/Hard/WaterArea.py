def waterArea(heights):
    #Name: Water Area
	#Category and difficulty: Dymamic Programming, Hard
    #time: O(n ) for 2 passes of array
	#space: O(n) for extra array created
    if(len(heights) == 0):
        return 0

    leftPtr = 0
    rightPtr = len(heights)-1
    waterAmount = 0
    leftMax = float('-inf')
    rigthMax = float('-inf')

    
    while(leftPtr < rightPtr):
        #Water depends on smaller amount, so when left < right, we use left to calculate amount
        if(heights[leftPtr] < heights[rightPtr]):
            if(heights[leftPtr] >= leftMax):
                leftMax = heights[leftPtr]
            else:
                waterAmount += leftMax-heights[leftPtr]
            leftPtr += 1
        else:
            if(heights[rightPtr] >= rigthMax):
                rigthMax = heights[rightPtr]
            else:
                waterAmount += rigthMax-heights[rightPtr]
            rightPtr -= 1
    
    return waterAmount

