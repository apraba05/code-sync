class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0

        
        while left < right:
            width = right - left
            if(height[left] < height[right]):
                hgt = height[left]
            else:
                hgt = height[right]
            
            print(hgt)
            print(width)

            if(len(height) == 2):
                area = hgt * 1
            else:
                area = hgt * width
            
            if(area > max_area):
                max_area = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

                

        return max_area