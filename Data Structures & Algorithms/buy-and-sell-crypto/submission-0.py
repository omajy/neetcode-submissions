class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        highest_profit = 0
        
        for index, price in enumerate(prices):
            left_window = prices[0:index+1]
            right_window = prices[index:]
       
            buy = min(left_window)
            sell = max(right_window)

            profit = sell - buy
            
            if profit > highest_profit:
                highest_profit = profit

        return highest_profit
