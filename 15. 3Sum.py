# Sort thr array. Move one pointer from start to end and keep performing 2 sum on remaining array. O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        l = len(nums)
        nums = sorted(nums)
        
        for i in range(l):
            p, q = i+1, l-1
            t = -nums[i]
            while p < q:
                if nums[p] + nums[q] < t:
                    p += 1
                elif nums[p] + nums[q] > t:
                    q -= 1
                else:
                    res.add((nums[i], nums[p], nums[q]))
                    p += 1
                    q -= 1
        return [list(x) for x in res]
        