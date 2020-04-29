# s1 and s2 can be represented as xy and yx. Both x and y are contained in xyxy. | return bool(B in A+A and len(A)==len(B))

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return bool(B in A+A and len(A)==len(B))