from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = defaultdict()
        indices = []

        for i in range (len(nums)):
            numsMap[nums[i]] = target - nums[i]
            if(numsMap[nums[i]] in nums):
                if(numsMap[nums[i]] == nums[i]):
                    continue
                else:
                    indices.append(i)
            else:
                continue
        
        return indices