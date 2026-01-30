from collections import defaultdict 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_new = set(nums)
        current_longest = 1

        if(len(nums_new) == 1):
            return 1

        for j in nums_new:
            i = 1
            while (j + i in nums_new):
                i += 1
            current_longest = max(current_longest,i)
        
        return current_longest