# Use a stack. Push opening braces in stack. For closing braces, pop the top of stack if matching else return False.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for i in s:
            if i in start:
                stack.append(i)
            elif stack and start[stack[-1]]==i:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
