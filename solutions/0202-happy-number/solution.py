class Solution:
    def nums_dig(self, n: int)-> list:
        return [int(d) for d in str(n)]

    def isHappy(self, n: int) -> bool:
        seen=set()
        while n not in seen and n!=1 :
            seen.add(n)
            n=sum([d**2 for d in self.nums_dig(n)])
            
       
        return n==1
        
           
