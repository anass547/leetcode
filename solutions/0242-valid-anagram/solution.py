class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)):
            return False
        for l in set(s):
            if s.count(l)!=t.count(l):
                return False
        return True
