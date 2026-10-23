class Solution:
    def hIndex(self, c: list[int]) -> int:
        c.sort(reverse=True) 
        h=0
        for i,x in enumerate(c):
            if x>=i+1:
                h+=1
            else:
                break
        return h
                
        
        
        
        
