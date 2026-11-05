class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        l1=[0]
        for i in range(1,len(s)):
            if s[i] not in s[:i]:
                l1.append(max(l1)+1)
            else:
                l1.append(l1[s.index(s[i])])
        l2=[0]
        for i in range(1,len(t)):
            if t[i] not in t[:i]:
                l2.append(max(l2)+1)
            else:
                l2.append(l2[t.index(t[i])])    
        
        return l1==l2
        
