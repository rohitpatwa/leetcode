# Same as finding start point of cycle in a linkedlist. Use fp, sp. They will intersect at one point. Start another pointer at beginning and let it intersect sp.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sp, fp = nums[0], nums[0]

        sp = nums[sp]
        fp = nums[fp]
        fp = nums[fp]
        
        while sp!=fp:
            sp = nums[sp]
            
            fp = nums[fp]
            fp = nums[fp]
            
        a = nums[0]
        b = sp
        
        while a!=b:
            a = nums[a]
            b = nums[b]
        return a