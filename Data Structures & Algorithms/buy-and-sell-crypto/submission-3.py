class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0 or len(prices) == 1:
            return 0

        left = 0
        right = 1 

        max_profit = 0 
        min_buy = prices[0]

        while right < len(prices):

            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if prices[right] < min_buy:
                min_buy = prices[right]
                left = right

            print(prices[left], prices[right], min_buy, max_profit)

            right += 1

        return max_profit



