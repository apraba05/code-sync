class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right = len(nums) - 1
        left = 0

        while (left <= right):
            if (nums[left] < nums[right] and nums[left] == 0):
                left += 1
            elif(nums[left] < nums[right] and nums[left] != 0):
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                right -= 1
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right -= 1
                
        
        print(nums)