class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_word=min(strs, key=len)
        
        w=""
        len_pre=[0]*len(strs)
        if len(shortest_word)==0:
            return w
        if len(strs)==1:
            return strs[0]
        j=0
        for l in shortest_word :
            w+=l
            j+=1
            for i,word in enumerate(strs):
                if w == word[:j]:
                    len_pre[i]+=1
                
        return shortest_word[:min(len_pre)]

            
