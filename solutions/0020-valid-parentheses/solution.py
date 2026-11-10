class Solution:
    def isValid(self, s: str) -> bool:
        o=[]
        d={"[":"]","(":")","{":"}"}

        
        for i in s:
            if i in d.keys():
                o.append(i)
            elif i in d.values():
                if len(o)==0:
                    return False
                if i==d[o[-1]]:
                    o.pop()
                else:
                    return False
       
        return len(o)==0
