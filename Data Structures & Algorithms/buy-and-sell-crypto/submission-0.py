class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            sell_arr = prices[i+1:]
            print("sell prices: ", sell_arr)
            sell = max(sell_arr)
            print("buy: ", buy)
            print("sell: ", sell)
            profit = max(profit,sell - buy)
            print ("Profit: ",profit)
        return profit