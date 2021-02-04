# Store all the valid replacements in a list and sort them desc. The apply each change on S.

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        changes = []
        
        for i in range(len(indexes)):
            start = indexes[i]
            word = sources[i]
            if S[start:start+len(word)] == word:
                changes.append((start, sources[i], targets[i]))
                
        changes.sort()                
        
        
        for c in changes[::-1]:
            
            start = c[0]
            end = start + len(c[1])
            
            S = S[:start] + c[2] + S[end:]
        return S