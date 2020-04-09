# Sorting each word is a linear time operation(counting sort). Sort each word and add it to a dictionary whose values are lists of words.

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for word in strs:
            w = tuple(sorted(word))
            res[w] = res.get(w, []) + [word]
        return list(res.values())
        