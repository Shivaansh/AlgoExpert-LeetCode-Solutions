def sortStack(stack):
    #Name: Sort Stack
    #Category and difficulty: Stack, Medium
    #time: O(n^2) as approach used is similar to insertion sort
	#space: O(n) for max depth of stack and recursive call

    #Edge case: Empty stack is always sorted
    if(len(stack) == 0):
        return stack
    
    current = stack.pop()
    sortStackHelper(stack, current)
    return stack

def sortStackHelper(stack, current):
    #Approach similar to insertion sort
    #Base Case
    if(len(stack) == 0):
        stack.append(current)
        return stack
    #Recursive Call - returns a SORTED stack
    sortStackHelper(stack, stack.pop())

    #Push current to a SORTED stack
    sortedStack = []
    while(len(stack) > 0 and stack[len(stack)-1] > current):
        sortedStack.append(stack.pop())
    stack.append(current)
    while(len(sortedStack) is not 0):
        stack.append(sortedStack.pop())
    return stack
    
    
