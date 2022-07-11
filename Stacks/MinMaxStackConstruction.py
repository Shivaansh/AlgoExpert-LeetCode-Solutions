# Feel free to add new properties and methods to the class.
class MinMaxStack:
    #Name: Min Max Stack Construction
    #Category and difficulty: Stacks, Medium

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []
    
    def peek(self):
        #O(1) time since just getting last value
        #O(1) space since a stack is already in use by class and no extra space is used
        return self.stack[-1]
        pass

    #Note: Pop and Push are the two functions which need to update max and min stacks, key takeaway here
    def pop(self):
        #O(1) time since just getting last value of stacks
        #O(1) space since a stack is already in use by class and no extra space is used
        if(len(self.stack)>0):
            number = self.stack.pop()
            if(number == self.minStack[-1]):
                self.minStack.pop()
            if(number == self.maxStack[-1]):
                self.maxStack.pop()
            return number
        return None

    def push(self, number):
        #O(1) time since just getting last value of stacks
        #O(1) space since a stack is already in use by class and no extra space is used
        self.stack.append(number)
        if(len(self.minStack) == 0 or number <= self.minStack[-1]):
            self.minStack.append(number)
        if(len(self.maxStack) == 0 or number >= self.maxStack[-1]):
            self.maxStack.append(number)

    def getMin(self):
        #O(1) time since just getting last value of minStack
        #O(1) space since a stack is already in use by class and no extra space is used
        if(len(self.minStack) > 0):
            return self.minStack[-1]
        return None
        pass

    def getMax(self):
        #O(1) time since just getting last value of maxStack
        #O(1) space since a stack is already in use by class and no extra space is used
        if(len(self.maxStack) > 0):
            return self.maxStack[-1]
        return None
        pass
