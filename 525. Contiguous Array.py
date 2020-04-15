# Calculate sum at each index. Two points between which sum repeats itself contains equal 0s and 1s

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = {0:-1}  # counter of sums at each index
        s = 0  # Sum at each index
        max_len = 0  # Max len of subarray
        
        for i, x in enumerate(nums):
            if x:
                s += 1 
            else:
                s -= 1
            
            if s in counter: # if we have seen that sum before
                max_len = max(max_len, i-counter[s])
            else:
                counter[s] = i
        return max_len