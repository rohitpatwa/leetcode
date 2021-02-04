# Linear time constant space. Create a counter of str. Then iterate over chars of str, when ctr[str[i]]==1, return i.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = Counter(s)
        
        for i, c in enumerate(s):
            if ctr[c] == 1:
                return i
        
        return -1