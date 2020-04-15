# In 2 for loops, we can compute prod of all numbers to the left and right of a given index. Multiply elements of these arrays and we get the result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod, right_prod = nums.copy(), nums.copy()
        
        left_prod[0] = 1
        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        
        right_prod[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]
        print(right_prod)
        return [left_prod[i]*right_prod[i] for i in range(len(nums))]
    



# This is a space optimized solution. We use output array to compute left prods. Then we use R to hold right prods as we traverse from right to left.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = nums.copy()
        res[0] = 1
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        R = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * R
            R = R*nums[i]
        return res