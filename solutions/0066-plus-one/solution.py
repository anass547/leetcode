class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=0
        for i,d in enumerate(digits):
            
            n+=d*(10**(len(digits)-i-1))
        n+=1
        return [int(d) for d in str(n)]
