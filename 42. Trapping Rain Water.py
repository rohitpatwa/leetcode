# 2 sols. One with O(n) space, 2 aux array storing left_max and right_max till point i. Other using 2 pointers (l, r) and constant space.

class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        left_max, right_max = 0,0
        total = 0
        
        while left < right:
            if height[left] <= height[right]:
                if height[left] < left_max:
                    total += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    total += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return total

class Solution:
    def trap(self, height: List[int]) -> int:

        
        left = [0]*len(height)
        right = [0]*len(height)
        
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        
        total = 0
        for i in range(len(height)):
            total += max(min(left[i], right[i]) - height[i], 0)
            
        return total