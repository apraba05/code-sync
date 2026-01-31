class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        stack = []

        for t in temperatures:
            stack.append(t)   
        stack.reverse()

        while (len(stack) > 0):
            start_len = len(days)
            if (len(stack) == 1):
                stack.pop()
                days.append(0)
                continue

            last = len(stack) - 1
            second_last = len(stack) - 2

            if(len(stack) == 2):
                if(stack[1] < stack[0]):
                    print("appending length 2")
                    stack.pop()
                    days.append(1)
                else:
                    stack.pop()
                    days.append(0)
                continue
            
         
            if (stack[last] < stack[second_last]):
                    diff = last - second_last
                    stack.pop()
                    days.append(diff)
                    print("greater than")
            elif (stack[last] > stack[second_last]):
                    found = False
                    last = len(stack) - 1
                    second_last = len(stack) - 2
                    print("less than")
                    while(second_last >= 0):
                        if(stack[last] < stack[second_last]):
                            diff = last - second_last
                            print(diff)
                            stack.pop()
                            days.append(diff)
                            found = True
                            break
                        else:
                            second_last -= 1

                    if not found:
                        stack.pop()
                        days.append(0)
                    continue


            else:
                    stack.pop()
                    days.append(0)
                    continue

        return days