# Use two pointers, one at beginning, one at end

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        
        while(i<j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
            # print(i, j, s)
        return s