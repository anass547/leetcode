class Solution(object):
    def convert(self, s, numRows):
        out=[""]*numRows
        res=""
        index=0
        k=1
        out[0]+=s[0]
        if numRows==1:
            return s
        while k<len(s):
            if index==0 :
                i=1           
            if index==numRows-1: 
                i=-1 
            index+=i    
            out[index]+=s[k]

            k+=1
        for j in range(numRows):
            res+=out[j]

        return res
