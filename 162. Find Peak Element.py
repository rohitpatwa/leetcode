# Call helper with (nums, l, r). if nums[m] < nums[m+1]: l = m+1; else: r = m-1.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        self.nums = nums
        return self.helper(0, len(nums)-1)
        
    def helper(self, l, r):
        m = (l+r)//2
        
        # Check for edge case
        if (m==0 or self.nums[m]>self.nums[m-1]) and \
            (m==len(self.nums)-1 or self.nums[m]>self.nums[m+1]):
            return m
        
        elif self.nums[m] < self.nums[m+1]:
            return self.helper(m+1, r)
        
        else:
            return self.helper(l, m-1)