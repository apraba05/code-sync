from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)

        for i in range (len(nums)):
            hashmap[nums[i]].append(i)
        print(hashmap)

        for funct in hashmap.values():
            if len(funct) > 1:
                return True
        
        return False