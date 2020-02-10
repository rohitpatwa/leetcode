# Two pointers, start and end. If start is smaller, start++, else end--. Calculate capacity at each step, return max.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_capacity = 0
        i, j = 0, len(height)-1
        
        while (i<j):
            capacity = min(height[j], height[i])*(j-i)
            max_capacity = max(max_capacity, capacity)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_capacity