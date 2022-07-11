def sunsetViews(buildings, direction):
    #Name: Sunset Views
    #Category and difficulty: Stacks, Medium
    #time: O(n) where n is length of the buildings array
    #space: O(n) for max possible size of stack

    #create STACK
    stack = [0]

    if(len(buildings) == 0):
        return []
    elif(len(buildings) == 1):
        return stack

    #Case for east
    if(direction == "EAST"):
        for index in range(1, len(buildings)):
            currentHeight = buildings[index]
            while(len(stack) > 0 and currentHeight >= buildings[stack[-1]]):
                stack.pop()
            stack.append(index)
        return stack
    #Case for west
    else:
        for index in range(1, len(buildings)):
            currentHeight = buildings[index]
            if(currentHeight > buildings[stack[-1]]):
                stack.append(index)
        return stack

