# Use two pointers i,j. Increment both if same char else j+=1. If i reaches the end, return True.

def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    i, j = 0, 0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
            j+=1
        else:
            j+=1
    return i==len(s)

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         t = iter(t)
#         return all(item in t for item in s)