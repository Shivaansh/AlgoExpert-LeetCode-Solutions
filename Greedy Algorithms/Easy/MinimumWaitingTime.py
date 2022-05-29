def minimumWaitingTime(queries):
    #Name: Minimum waiting time
    #Category and difficulty: Greedy Algorithms, Easy
    #time: O(n log n) since we sort the input array
    #space: O(1)
    queries.sort()
    totalTime = 0
    currentTime = 0
    for index in range(len(queries)):
        if(index == 0):
            currentTime += 0
        else:
            currentTime += queries[index - 1]
            totalTime += currentTime
    return totalTime
    