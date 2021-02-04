# Use 2 pointers l=0, r=n-1. Iterate over the array, if i==0, swap with left and (l++, i++). If i==2, swap with rigth and (r++). Else i==1 (i++).

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, i = 0, len(nums)-1, 0
        
        while i<=right:
            if nums[i] == 1:
                i += 1
            elif nums[i]==0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1