class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketStartClose = {
        ")":"(",
        "}":"{",
        "]":"["
        }

        for i in s:
                if i in bracketStartClose:
                    if stack and stack[-1] == bracketStartClose[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
        
        return True if not stack else False