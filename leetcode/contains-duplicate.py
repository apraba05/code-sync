from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)

        for i in nums:
            hashmap[nums[i-1]].append(nums[i-1])

        for hash in hashmap.values():
            if(len(hash) > 1):
                return True
            else:
                return False