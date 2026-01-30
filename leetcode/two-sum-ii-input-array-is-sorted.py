class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        arr = []
        print(numbers[0])

        while left <= right:
            if ((numbers[left] + numbers[right]) == target):
                arr.append(left+1)
                arr.append(right+1)
                return(arr)
            elif(target < (numbers[left] + numbers[right])):
                right -= 1
            else:
                left += 1