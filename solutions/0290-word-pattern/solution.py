class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=list(s.split(" "))
        if len(l)!=len(pattern):
            return False
        return len(set(l))==len(set(pattern))==len(set(zip(l,pattern)))
