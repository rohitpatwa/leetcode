# Sort nums. Run and fix i from 1 to n-2. Run j=i+1, k=n-1. if nums[i]+nums[j]+nums[k]<target, count+= k-j, j+1; else: k-= 1.

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            j, k = i+1, len(nums) - 1
            
            while j < k:
                if nums[i] + nums[j]+nums[k] < target:
                    count += k-j
                    j += 1
                else:
                    k -= 1
        return count