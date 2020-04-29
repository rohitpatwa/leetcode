# Find the pivot element i using BS. l=i, r=i+n-1. Do normal bs between l and r and check arr[m%n].

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums)==1 or (nums[0] < nums[-1]):
            i = 0
        else:
            i = 1
            while nums[i] > nums[i-1]:
                i += 1
        
        n = len(nums)
        l, r = i, i+n-1

        while l <= r:
            m = (l+r)//2
            if nums[m%n] == target:
                return m%n
            elif nums[m%n] < target:
                l = m+1
            else:
                r = m-1
        return -1