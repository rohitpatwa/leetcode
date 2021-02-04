# Go from right to left in inc order. Stop at smaller element, call it pivot. Reverse the arr on right of pivot and swap pivot with next greater element.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        if len(nums) == 2:
            nums.reverse()
            return
        pivot = len(nums) - 2

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        self.reverse(nums, pivot + 1, len(nums) - 1)

        if pivot==-1:
            return nums

        next_num = pivot + 1

        while nums[next_num] <= nums[pivot]:
            next_num += 1

        self.swap(nums, pivot, next_num)
        return nums


    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
