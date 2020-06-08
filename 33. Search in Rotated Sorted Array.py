# Find the pivot element i using BS. l=i, r=i+n-1. Do normal bs between l and r and check arr[m%n].

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n-1
        
        if nums[l] < nums[r]:
            pass # The array is not rotated
        else:
            while l<r:
                m = (l+r)//2
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m+1
        
        l, r = l, l+n-1
        
        # Assume the array is starting at l and going till r
        # Now perform normal binary search
        # Only when calling nums[x], use %n to keep the indices within bounds
        # Return the middle found in the assumed array as m%n
        
        while l<=r:
            m = (l+r)//2
            if nums[m%n] < target:
                l = m+1
            elif nums[m%n] > target:
                r = m-1
            else:
                return m%n
        return -1
