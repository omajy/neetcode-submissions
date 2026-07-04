class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0 or len(prices) == 1:
            return 0

        left = 0
        right = 1

        lowest_price = prices[0]

        max_profit = 0

        while right != len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)

            if prices[right] < lowest_price:
                lowest_price = prices[right]
                left = right
            
            print('right:', right, 'left:', left, 'max profit:', max_profit)
            right += 1
        
        return max_profit
        