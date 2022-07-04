def taskAssignment(k, tasks):
    #Name: Task Assignment
    #Category and difficulty: Greedy Algorithms, Easy
    #O(n) time and space, n = 2k is length of tasks array
    indexMap = {}
    for index in range(len(tasks)):
        task = tasks[index]
        if(task not in indexMap):
            indexMap[task] = []
        indexMap[task].append(index)

    #O(n log n) time, using sorting
    tasks = sorted(tasks)
    array = []
    
    lo = 0
    hi = len(tasks)-1

    #O(n) time since length of tasks is 2k
    while(lo < hi):
        array.append([tasks[lo], tasks[hi]])
        lo += 1
        hi -= 1

    #O(n) time
    for set in array:
        minVal = set[0]
        maxVal = set[1]

        set[0] = indexMap[minVal].pop()
        set[1] = indexMap[maxVal].pop()           
    return array
