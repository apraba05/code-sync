from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = defaultdict(int)
        arr = []
        for i in range len(nums):
            nums[nums[i]].append(i)
            if (len nums[nums[i]].value() > 1):
                arr.append(nums.value())
                
        if (arr[0] == arr[1] and abs(arr[0] - arr[1] <= k)):
            return True
        
        return False