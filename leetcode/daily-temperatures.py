class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        stack = []

        for t in temperatures:
            stack.append(t)   
        stack.reverse()

        for i in stack:
            last = len(stack) - 1
            second_last = len(stack) - 2
            if (stack[second_last] < 0):
                stack.pop()
                days.append(0)
            if (stack[last] < stack[second_last]):
                diff = last - second_last
                stack.pop()
                days.append(diff)
            elif (stack[last] > stack[second_last]):
                    last = len(stack) - 1
                    second_last = len(stack) - 2
                while(second_last >= 0):
                    if(stack[last] < stack[second_last]):
                        diff = last - second_last
                        stack.pop()
                        days.append(diff)
                        last -= 1
                    elif (stack[last] == 1 and stack[second_last] == 0):
                        stack.pop()
                        days.append(0)
                    else:
                        if(second_last < 0):
                            break
                        else:
                            second_last -= 1
            else:
                stack.pop()
                days.append(0)
            

        print(days)