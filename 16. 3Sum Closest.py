# Sort the array. Start one pointer at beginning, do two sum approach on the remaining array using two more pointers. Return minumim distance result


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        res = None
        diff = float('inf')
        
        for i in range(n-2):
            
            j, k = i+1, n-1
            
            while j<k:
                three_sum = nums[i] + nums[j] + nums[k]                
                
                if abs(target - three_sum) < diff:
                    res = three_sum
                    diff = abs(target - res)
                    
                if three_sum < target:
                    j += 1
                elif three_sum > target:
                    k -= 1
                else:
                    return res
        return res
                    