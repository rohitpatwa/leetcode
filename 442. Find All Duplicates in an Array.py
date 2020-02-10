# Go the index and set the number -ve of itself. Whenever you see an already -ve number, it is repeated.

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i])-1] *= -1
                
        return res