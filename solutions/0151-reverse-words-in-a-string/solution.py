class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split())
        a=""
        for i in range(len(l),1,-1):
            a+=l[i-1]+" "
        a+=l[0]
        return a
