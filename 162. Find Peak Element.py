# Call helper with (nums, l, r). if nums[m] < nums[m+1]: l = m+1; else: r = m-1.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, l, r):
        m = (l+r)//2
        
        if (m==l or nums[m]>nums[m-1]) and (m==r or nums[m]>nums[m+1]):
            return m
        elif nums[m] < nums[m+1]:
            return self.helper(nums, m+1, r)
        else:
            return self.helper(nums, l, m-1)