class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        middle = len(nums) // 2 - 1
        right = len(nums) - 1
        nums = sorted(nums)
        threeSumList = list()
        
    
        while(left != middle != right):
                if(nums[left] + nums[middle] + nums[right] > 0):
                    right -= 1
                    print("decreasing right")
                elif(nums[left] + nums[middle] + nums[right] < 0):
                    left += 1
                    print("increasing left")
                elif(nums[left] + nums[middle] + nums[right] == 0):
                    temp = []
                    print("adding array")
                    temp.append(nums[left])
                    temp.append(nums[middle])
                    temp.append(nums[right])
                    threeSumList.append(temp)
                    if(middle + 1 == right):
                        left += 1
                    else:
                        middle += 1
                else:
                    continue
                    print("else loop")

        return(unique)