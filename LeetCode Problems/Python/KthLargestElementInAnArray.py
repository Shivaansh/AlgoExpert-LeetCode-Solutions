#Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Name: Kth Largest Element in an Array
# Difficulty: Medium
# Topic: Min Heap
#Time: O(n log k) since we update the root a maximum of n times, each update is a log k operation
#Space: O(k) for size of heap used
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if(k > len(nums)):
            return
        
        #Initialize Heap
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        #Update heap
        for i in range(k, len(nums)):
            root = minHeap[0]
            if(nums[i] >= root):
                removed = heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        #return lowest number in heap       
        return heapq.heappop(minHeap)