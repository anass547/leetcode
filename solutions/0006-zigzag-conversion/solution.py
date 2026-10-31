class Solution:
    def convert(self, s: str, numRows: int) -> str:
        c=0
        down=True
        zigzag=[""]*numRows
        if numRows==1:
            return s
        for l in s:
            
            if down==True:
                zigzag[c]+=l
                
            elif down==False:
                zigzag[numRows-c-1]+=l
            c=c+1    
            
            if c==numRows and down==True:
                c=1
                down=False
            elif c==numRows and down==False:
                c=1
                down=True
            
        return ''.join(zigzag)
        


