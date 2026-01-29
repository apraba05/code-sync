from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        new_nums = defaultdict(list)
        for i in range (len(nums)):
            new_nums[nums[i]].append(i)
            if (len (new_nums[nums[i]]) > 1):
                new_var = new_nums[nums[i]]
        print(new_var)
        if (nums[new_var[0]] == nums[new_var[1]] and abs(new_var[0] - new_var[1] <= k)):
             return True
        
        return False