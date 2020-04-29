# Maintain a counter. '(' -> +1, ')' -> -1. Whenever counter is 0, remove first and last parentheses. Call recursively.


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = 0
        for i in range(len(S)):
            if S[i]=='(':
                counter += 1
            else:
                counter -= 1
            if counter==0:
                return S[1:i] + self.removeOuterParentheses(S[i+1:])      
        return ''
        
#         if not S:
#             return ''
#         self.counter = 0
#         return self.helper(S)
                
                
#     def helper(self, s):
#         for i in range(len(s)):
#             if s[i]=='(':
#                 self.counter += 1
#             else:
#                 self.counter -= 1
#             if self.counter==0 and i!=0:
#                 return s[1:i] + self.helper(s[i+1:])            
#         return ''