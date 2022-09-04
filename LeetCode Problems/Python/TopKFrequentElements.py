#https://docs.python.org/3/library/heapq.html
#https://www.programiz.com/python-programming/methods/dictionary/get

#Link: https://leetcode.com/problems/top-k-frequent-elements/
# Name: Top K Frequent Elements
# Difficulty: Medium
# Topic: Min Heap
#Time: O(n log k) since we update the root a maximum of n times, each update is a log k operation
#Space: O(n + k) for size of heap used and the hashmpa size
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        
        freqMap = {}
        for num in nums:
            if(num not in freqMap):
                freqMap[num] = 0
            freqMap[num] += 1
        
        return heapq.nlargest(k, freqMap.keys(), key=freqMap.get)
        
        