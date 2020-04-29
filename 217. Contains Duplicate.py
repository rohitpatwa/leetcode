# Create a set and check if element already exists.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(nums) != len(set(nums))