# Use fast pointer, slow pointer approach. Move slow pointer if arr[slow] != 0. Move fast always, When arr[slow]==0, swap slow fast values.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[slow]==0 and nums[fast]!=0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow]!=0:
                slow += 1

            fast += 1

        return nums