class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        for l in set(ransomNote):
            if ransomNote.count(l)>magazine.count(l):
                return False
        
        return True
        
        
