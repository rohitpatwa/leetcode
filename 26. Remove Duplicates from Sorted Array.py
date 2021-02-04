# 2 Pointer approach. i=0; j in range(1, n). Where n[i]!=n[j], increment i and swap n[i], n[j].

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)<=1:
            return len(nums)
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1