# Code for Min Heap
import heapq

# Create an array
minHeap = []

# Heapify the array into a Min Heap
heapq.heapify(minHeap)

# Add 3，1，2 respectively to the Min Heap
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 1)
heapq.heappush(minHeap, 2)

# Check all elements in the Min Heap, the result is [1, 3, 2]
print("minHeap: ", minHeap)

# Get the top element of the Min Heap
peekNum = minHeap[0]

# The result is 1
print("peek number: ", peekNum)

# Delete the top element in the Min Heap
popNum = heapq.heappop(minHeap)

# The result is 1
print("pop number: ", popNum)

# Check the top element after deleting 1, the result is 2
print("peek number: ", minHeap[0])

# Check all elements in the Min Heap, the result is [2,3]
print("minHeap: ", minHeap)

# Check the number of elements in the Min Heap
# Which is also the length of the Min Heap
size = len(minHeap)

# The result is 2
print("minHeap size: ", size)

# Maintain a heap of keys by sorting on the value, for dictionaries
heapq.nlargest(k, hashmap.keys(), key=hashmap.get)

# Code for Max Heap
# import heapq

# Create an array
maxHeap = []

# Heapify the array into a Min Heap
# we need to negate each element to convert the Min Heap to a Max Heap
heapq.heapify(maxHeap)

# Add 1，3，2 respectively to the Max Heap
# Note we are actually adding -1, -3 and -2 after negating the elements
# The Min Heap is now converted to a Max Heap
heapq.heappush(maxHeap, -1 * 1)
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)

# Check all elements in the Max Heap, the result is [-3, -1, -2]
print("maxHeap: ", maxHeap)

# Check the largest element in the Heap, which is min value in the -1 * Heap
peekNum = maxHeap[0]

# The result is 3
print("peek number: ", -1 * peekNum)

# Delete the largest element in the Max Heap
# Which is the smallest value in the current Heap
popNum = heapq.heappop(maxHeap)

# The result is 3
print("pop number: ", -1 *  popNum)

# Check the largest element after deleting 3, the result is 2
print("peek number: ", -1 * maxHeap[0])

# Check all elements in the Max Heap, the result is [-2,-1]
print("maxHeap: ", maxHeap)

# Check the number of elements in the Max Heap
# Which is also the length of the Min Heap
size = len(maxHeap)

# The result is 2
print("maxHeap size: ", size)