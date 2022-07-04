def taskAssignment(k, tasks):
    #Name: Task Assignment
    #Category and difficulty: Greedy Algorithms, Easy
    #O(n^2) time and O(n) space, n = 2k is length of tasks array
    minTasks = []
    maxTasks = []
    array = []

    #O(n * n) where n = 2k is length of tasks array
    for i in range(k):
        max = -9999999
        min = 99999999
        maxIndex = -1
        mindIndex = -1
        #find max and min, this is an O(n) operation
        for index in range(len(tasks)):
            if(tasks[index] >= max and index not in maxTasks and index not in minTasks):
                max = tasks[index]
                maxIndex = index
            if(tasks[index] < min and index not in maxTasks and index not in minTasks):
                min = tasks[index]
                minIndex = index   
        maxTasks.append(maxIndex)  
        minTasks.append(minIndex)
    for index in range(k):
        array.append([maxTasks[index], minTasks[index]])
    return array
