# Create a helper which checks for palindrome. Return helper(a, b) or helper(b, a).

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a, b):
            i, j = 0, len(a)-1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
                
            return a[i:j+1] == a[i:j+1][::-1] or b[i:j+1] == b[i:j+1][::-1]
        
        return check(a, b) or check(b, a)