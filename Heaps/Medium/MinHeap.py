# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        # self.heap is represented as an array, so just return a modified array via buildHeap method
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # siftDown parents starting from last parent IN PLACE
        # time: O(n)
        # space: O(n) for given array, no extra space since in-place
        parent = (len(array) - 2)//2
        for index in reversed(range(parent+1)):
            self.siftDown(index, len(array)-1, array)
        return array
        
    def siftDown(self, currIndex, limit, arr):
        # compare to both children and swap with LOWER child if both smaller, else swap with the child that is smaller than current
        # time: O(log n)
        # space: O(1) coz no extra space
        firstChildIndex = (2 * currIndex) + 1
        
        while(firstChildIndex <= limit):
            indexToSwap = firstChildIndex
            # determine child to swap with
            secondChildIndex = (2 * currIndex) + 2
            if(secondChildIndex <= limit and arr[secondChildIndex] < arr[firstChildIndex]):
                indexToSwap = secondChildIndex 
            #keep swapping if needed
            if(arr[indexToSwap] < arr[currIndex]):
                temp = arr[currIndex]
                arr[currIndex] = arr[indexToSwap]
                arr[indexToSwap] = temp
                #swap indices so current is at new child
                currIndex = indexToSwap
                firstChildIndex = (2 * currIndex) + 1
            else:
                # return if swap not needed
                return

    def siftUp(self, currIndex, arr):
        # compare to parent and swap if parent bigger than current
        # time: O(log n)
        # space: O(1) coz no extra space
        parentIndex = (currIndex - 1) // 2
        while(currIndex > 0 and arr[parentIndex] > arr[currIndex]):
            temp = arr[parentIndex]
            arr[parentIndex] = arr[currIndex]
            arr[currIndex] = temp
            #update indices so current is new parent, get new parent
            currIndex = parentIndex
            parentIndex = (currIndex - 1) // 2

    def peek(self):
        # return FIRST element of heap
        # time: O(1)
        # space: O(1) coz no extra space
        return self.heap[0]

    def remove(self):
        # swap root and last value, remove current root from end of array then sift down new root
        # time: O(log n) coz of siftDown operation
        # space: O(1) coz no extra space
        temp = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap[len(self.heap)-1] = temp
        
        value = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return value

    def insert(self, value):
        # add new value to end of array and then sift up repeatedly
        # time: O(log n) coz of siftUp operation
        # space: O(1) coz adding 1 extra element to array
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
