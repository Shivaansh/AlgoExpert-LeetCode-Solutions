#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Name: Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Topic: Array
#Time: O(n) for 1 iteration through array
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        costPrice = float('inf')
        profit = 0
        for price in prices:
            #Buy a stock
            if(price < costPrice):
                costPrice = price
            #Sell a stock if profitable and buy on the same day
            else:
                if(price - costPrice > 0):
                    profit += (price - costPrice)
                    costPrice = price
        return profit