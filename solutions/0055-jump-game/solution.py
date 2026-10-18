class Solution:
    def canJump(self, n: list[int]) -> bool:
        k=True
        if len(n)==1:
            return True
        if n[0]==0:
            return False
        for i in range(len(n)-1):
            if n[i]==0:
                for j in range(i):
                    if n[j]<=i-j:
                        k=False
                        
                    else :
                        k=True
                        break
                if k==False:
                    return k
            
            
        return k
            


