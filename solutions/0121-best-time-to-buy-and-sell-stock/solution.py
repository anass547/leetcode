class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        mini=prices[0]
        for p in prices:
            if p<mini:
                mini=p
            elif profit < p-mini:
                profit=p-mini
        return profit
