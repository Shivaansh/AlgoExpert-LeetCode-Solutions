def shiftedBinarySearch(array, target):
    #Name: Shifted Binary Search
	#Category and difficulty: Searching, Hard
    #time: O(log n) in shifted sorted array
	#space: O(1)
    lo = 0
    hi = len(array)-1

    

    while(lo < hi):
        mid = int((lo + hi)/2)
        midVal = array[mid]
        leftVal = array[lo]
        
        if(midVal == target):
            return mid
            
        elif(midVal > target):
            if(leftVal <= midVal):
                if(target < leftVal):
                    lo = mid+1
                else:
                    hi = mid-1
            else:
                if(target < leftVal):
                    hi = mid-1
                else:
                    lo = mid+1
        else:
            if(leftVal <= midVal):
                if(target < leftVal):
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if(target < leftVal):
                    lo = mid+1
                else:
                    hi = mid-1

    if(array[lo] == target):
        return lo
    return -1
