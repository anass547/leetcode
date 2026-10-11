class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        c = [1] * n
        for i in range(0,n-1):
            if ratings[i+1]>ratings[i] and c[i+1]<=c[i]:
                c[i+1]=c[i]+1
        for i in range(n-1,0,-1):
            if ratings[i-1]>ratings[i] and c[i-1]<=c[i]:
                c[i-1]=c[i]+1
        return sum(c)
        
