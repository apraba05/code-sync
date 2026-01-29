class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i,x in enumerate(nums):
            prev[x] = i
        
        for i,x in enumerate(nums):
            diff = target - x
            if diff in prev and prev[diff] != i:
                return[i,prev[diff]]
        
        return[]