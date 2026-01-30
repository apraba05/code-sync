class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        right = len(nums) - 1
        left = 0

        for right in range(len(nums)):
            if (nums[right] != 0):
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
        print(nums)