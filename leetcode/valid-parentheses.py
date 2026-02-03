class Solution:
    def isValid(self, s: str) -> bool:
        bracketStorage = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stringList = list(s)

        if (len(stringList) == 0):
            return True

        for i in stringList:
            if(stringList[i] in bracketStorage):
                stringList.pop()
            else:
                return False