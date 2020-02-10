# Start with 0. Take xor of all the numbers. ((0 xor a) xor a) = 0 | (((0 xor a) xor b) xor a) = b

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in nums:
            x = x^i
        return x