# Stupid extention of 3sum problem. n^3 solution. Two pointer approach inside double for loop.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        res = set()
        nums = sorted(nums)
        
        for i in range(l):
            for j in range(i+1, l):
                t = target - nums[i] - nums[j] 
                
                p, q = j + 1, l-1
                while p < q:
                    if nums[p] + nums[q] < t:
                        p += 1
                    elif nums[p] + nums[q] > t:
                        q -= 1
                    else:
                        res.add(tuple([nums[i], nums[j], nums[p], nums[q]]))
                        p += 1
                        q -= 1
        return [list(x) for x in res]