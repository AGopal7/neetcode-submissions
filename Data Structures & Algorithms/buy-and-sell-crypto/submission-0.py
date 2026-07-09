class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      lowest = prices[0]
      max_profit = 0
      for i in range (len(prices)):
        if lowest > prices[i]:
            lowest = prices[i]
        today_prof = prices[i]- lowest 
        if today_prof >max_profit:
            max_profit = today_prof
      return max_profit

        



        