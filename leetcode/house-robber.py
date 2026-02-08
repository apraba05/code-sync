class Solution:
    def rob(self, nums: List[int]) -> int:
        maxNums = 0
        indexEven = 0
        indexOdd = 1
        maxOdd = 0
        maxEven = 0
        

        while(indexOdd <= (len(nums)-1)):
            maxOdd += nums[indexOdd]
            indexOdd += 2
        
        while(indexEven <= (len(nums)-1)):
            maxEven += nums[indexEven]
            indexEven += 2
        
        maxNums = max(maxOdd,maxEven)

        return maxNums