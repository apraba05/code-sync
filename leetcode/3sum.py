class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        middle = len(nums) // 2
        right = len(nums) - 1
        nums = sorted(nums)
        print(nums)
        threeSumList = list()

        if(len(nums) > 3):
            middle = middle - 1
        
        while(left != middle != right):
                if(nums[left] + nums[middle] + nums[right] == 0):
                    temp = []
                    temp.append(nums[left])
                    temp.append(nums[middle])
                    temp.append(nums[right])
                    threeSumList.append(temp)
                    right -= 1
                elif(nums[left] + nums[middle] + nums[right] > 0):
                    if(middle+1 == right):
                        left += 1
                    else:
                        right -= 1
                elif(nums[left] + nums[middle] + nums[right] < 0):
                    if(middle-1 == left):
                        middle += 1
                    else:
                        left += 1
                else:
                    continue
        
        threeSumList = list(set(tuple(triplet) for triplet in threeSumList))

        return threeSumList