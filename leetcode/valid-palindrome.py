import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result_string = re.sub(r'[^a-z0-9]', '', s)
        ls = list(result_string)
        left = 0
        right = len(ls)-1


        if(len(ls) == 0):
            return True

        while left <= right:
            if (ls[left] == ls[right]):
                left += 1
                right -= 1
            else:
                return False
        
        return True