def waterArea(heights):
    #Name: Water Area
	#Category and difficulty: Dymamic Programming, Hard
    #time: O(n ) for 2 passes of array
	#space: O(n) for extra array created
    if(len(heights) == 0):
        return 0

    waterAtPillar = [0] * len(heights)

    #Forward pass
    max = heights[0]
    for index in range(1, len(heights)-1):
        currentHeight = heights[index]
        if(max >= currentHeight):
            waterAtPillar[index] = (max - currentHeight)  
        else:
            max = currentHeight

    #Reverse pass
    max = heights[len(heights)-1]
    for index in reversed(range(1, len(heights)-1)):
        currentHeight = heights[index]
        if(max < currentHeight):
            max = currentHeight
        waterAtPillar[index] = min(waterAtPillar[index], max - currentHeight)

    return(sum(waterAtPillar))

