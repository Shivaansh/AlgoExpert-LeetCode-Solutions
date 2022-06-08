def mergeOverlappingIntervals(intervals):
    #Name: Merge Overlapping Intervals
	#Category and difficulty: Arrays, Medium
    #time: O(n log n) since we sort the input array then iterate through it once
	#space: O(n) since the returned array can have max size same as input array
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    if(len(sortedIntervals) == 1):
        return sortedIntervals
    mergedIntervals = []
    index = 0
    while(index < len(sortedIntervals)-1):
        if(index ==  len(sortedIntervals)-2):
            if(sortedIntervals[index][1] >= sortedIntervals[index+1][0]):
                mergedIntervals.append([ sortedIntervals[index][0], max(sortedIntervals[index+1][1], sortedIntervals[index][1]) ])
                break
            else:
                mergedIntervals.append(sortedIntervals[index])
                mergedIntervals.append(sortedIntervals[index+1])
                break
        elif(sortedIntervals[index][1] >= sortedIntervals[index+1][0]):
            sortedIntervals[index][1] = max(sortedIntervals[index+1][1], sortedIntervals[index][1])
            sortedIntervals.pop(index+1)
        else:
            mergedIntervals.append(sortedIntervals[index])
            index += 1
    return mergedIntervals
