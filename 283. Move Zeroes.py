# Use fast pointer, slow pointer approach. Move slow pointer if arr[slow] != 0 or when we swap. Move fast always.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow, fast = 0, 0
        
        for fast in range(len(nums)):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            elif nums[slow] != 0:
                slow += 1
        return nums
                