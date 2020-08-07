# Pop first char and send the remaining array to a magic funciton which returns all perms. Place popped char at all positions in each perm.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        
        temp = [nums[0]]
        perms = self.permute(nums[1:])
        
        res = []
        
        for perm in perms:
            for i in range(len(perm) +1):
                combi = perm[:i] + temp + perm[i:]
                res.append(combi)
        
        return res




# Simulate swapping branches of a tree. Call helper with l pointer. for i in range(l, n), swap i, l. Recurse with l+1, backtrack 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, 0)
        return self.res
        
    def helper(self, nums, l):
        if l==len(nums)-1:
            self.res.append(nums[:])
            
        for i in range(l, len(nums)):
            nums[l], nums[i] = nums[i], nums[l]
            self.helper(nums, l+1)
            nums[l], nums[i] = nums[i], nums[l]
