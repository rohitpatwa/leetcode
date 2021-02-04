# Maintain i1, i2 to store latest occurance of w1 and w2. When you find w1, do res = min(res, i - i2). Same for w2.

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = float('-inf'), float('-inf')
        res = float('inf')
        for i, w in enumerate(words):
            if w==word1:
                res = min(res, i-idx2)
                idx1 = i
            elif w==word2:
                res = min(res, i-idx1)
                idx2 = i
            if res==1:
                return res
        return res
        