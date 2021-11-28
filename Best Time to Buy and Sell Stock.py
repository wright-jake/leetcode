#example input
prices = [7,1,5,3,6,4]

#solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set max profit to 0 so we can then only improve or make nothing as price cannot be less than 0
        max_profit = 0
        
        #set minimum price to infinity
        min_price = float('inf')
        
         #iterate through the list comparing the min price each time and then seeing if higher profit can be made
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit
