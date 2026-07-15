class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit= 0 
        for i in range (len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            today_max = prices[i]- lowest 
            if today_max > max_profit:
                max_profit = today_max 
        return max_profit
      
        