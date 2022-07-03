def bubbleSort(array):
    #Name: Bubble Sort
    #Category and difficulty: Sorting, Easy
    #time: O(n^2) 
	#space: O(1)
    for i in range(len(array)):
        #Put one element in sorted position
        for j in range(len(array)-1):
            if(array[j] > array[j+1]):
                #swap
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array
    pass

def insertionSort(array):
    #Name: Insertion Sort
    #Category and difficulty: Sorting, Easy
    #time: O(n^2) in the worst case
	#space: O(1)
    for i in range(1, len(array)):
        index = i
        while(index > 0 and array[index] < array[index-1]):
            #swap pairs
            array[index], array[index-1] = array[index-1], array[index]
            index -= 1
    return array

def selectionSort(array):
    #Name: Selection Sort
    #Category and difficulty: Sorting, Easy
    #time: O(n^2) 
	#space: O(1)
    for index in range(len(array)):
        #Swap with index
        min = index
        for j in range(index, len(array)):
            #Find smallest item to swap index with 
            if(array[j] < array[min]):
                min = j
        #perform swap, bring smallest number found yet to [index]
        temp = array[min]
        array[min] = array[index]
        array[index] = temp
    #return sorted array
    return array
