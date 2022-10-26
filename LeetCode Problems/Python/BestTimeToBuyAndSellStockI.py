#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Name: Best Time to Buy and Sell Stock I
# Difficulty: Easy
# Topic: Array
#Time: O(n) for 1 iteration through array
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        costPrice = float('inf')
        profit = 0
        for price in prices:
            #Find lowest purchase price
            if(price < costPrice):
                costPrice = price
            #Find profit and compare to max
            else:
                if(price - costPrice > profit):
                    profit = (price - costPrice)
        return profit
        
        