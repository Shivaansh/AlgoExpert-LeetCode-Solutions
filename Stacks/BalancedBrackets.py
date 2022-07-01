def balancedBrackets(string):
    #Name: Balanced Brackets
    #Category and difficulty: Stacks, Medium
    #time: O(n) where n is length of the string
    #space: O(n) for max possible size of stack
    
    stack = []

    for char in string:
        if(char == '{' or char == '[' or char == '('):
            stack.append(char)
        elif (char == ']'):
            if(len(stack) == 0):
                return False
            else:
                if(stack[-1] != '['):
                    return False
                else:
                    stack.pop()
        elif (char == '}'):
            if(len(stack) == 0):
                return False
            else:
                if(stack[-1] != '{'):
                    return False
                else:
                    stack.pop()
        elif (char == ')'):
            if(len(stack) == 0):
                return False
            else:
                if(stack[-1] != '('):
                    return False
                else:
                    stack.pop()
    return len(stack) == 0
                    
    pass
