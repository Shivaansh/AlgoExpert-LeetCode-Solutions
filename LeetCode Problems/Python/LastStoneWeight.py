#Link: https://leetcode.com/problems/last-stone-weight/
# Name: Last Stone Weight
# Difficulty: Easy
# Topic: Min Heap
#Time: O(n log n) since we update the root a maximum of n times, each update is a log k operation
#Space: O(n) for size of heap used
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        maxHeap = []
        heapq.heapify(maxHeap)
        for i in stones:
            heapq.heappush(maxHeap, -1 * i)
            
        while(len(maxHeap) > 1):
            stone1 = -1 * heapq.heappop(maxHeap)
            stone2 = -1 * heapq.heappop(maxHeap)
            dif = abs(stone1-stone2)
            if(dif > 0):
                heapq.heappush(maxHeap, -1*dif)
        
        if(len(maxHeap) > 0):
            return abs(maxHeap[0])
        else:
            return 0
        