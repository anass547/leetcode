class Solution:
    def maxProfit(self, p: list[int]) -> int:
        if len(p) < 2:
            return 0

        pr = 0
        for i in range(1, len(p)):
            pr+= max(0, p[i] - p[i - 1])
           

        return pr
