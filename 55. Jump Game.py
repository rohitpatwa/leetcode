# Keep calculating max reachable index from current index. If curr index passes max reachable index, return False

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Reverse array approach
        # last_valid_index = -1
        # for i in range(len(nums)-1, -1, -1):
        #     x = nums[i]
        #     if i+x >= last_valid_index:
        #         last_valid_index = i
        # return (last_valid_index==0)
    
        # Forward array approach
        max_reachable = 0
        for i,x in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + x)
            if max_reachable >= len(nums)-1:
                return True