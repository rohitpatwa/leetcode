# Use two pointer approach. Initiate one at beginning and one at the end.


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers)-1
        
        while True:
            s = numbers[i] + numbers[j]
            if s>target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [i+1, j+1]