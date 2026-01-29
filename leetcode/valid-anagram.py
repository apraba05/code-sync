class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = list(s)
        new_t = list(t)
        new_s.sort()
        new_t.sort()

        if(len(new_s) != len(new_t)):
            return False

        for i in range (len(new_s)):
            if(new_s[i] != new_t[i]):
                return False
        
        return True