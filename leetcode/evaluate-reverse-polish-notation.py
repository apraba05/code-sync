class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stackSymbols = []

        for i in range (len(tokens)):
            if(tokens[i] != '+' or tokens[i] != '*'                                                                                                                                                                                ):
                stack.append(tokens[i])
        print(stack)