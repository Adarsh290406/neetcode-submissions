class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumprice=prices[0]
        maximumprofit=0
        for i in range(len(prices)):
            if minimumprice>prices[i]:
                minimumprice=prices[i]
            profit=prices[i]-minimumprice
            if maximumprofit<profit:
                maximumprofit=profit
        return(maximumprofit)
