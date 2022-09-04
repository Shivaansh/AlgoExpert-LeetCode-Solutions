#Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Name: Kth Largest Element in a Stream
# Difficulty: Easy
# Topic: Min Heap
#Time: O(n log k) since we update the root a maximum of n times, each update is a log k operation
#Space: O(k) for size of heap used
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxSize = k
        self.minHeap = []
        heapq.heapify(self.minHeap)
        #prepare heap of at most k largest elements till now
        for i in range(k):
            if(i < len(nums)):
                heapq.heappush(self.minHeap, nums[i])
        for i in range(k, len(nums)):
            if(i < len(nums)):
                root = self.minHeap[0]
                if(nums[i] >= root):
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, nums[i])

    def add(self, val: int) -> int:
        #cases: there are k or k less than k elements in the heap
        if(len(self.minHeap) >= self.maxSize):
            root = self.minHeap[0]
            if(val >= root):
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
            
        return self.minHeap[0]