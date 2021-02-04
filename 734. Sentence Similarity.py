# Create a set of all pairs of similar words. Then iterate of zip(S1, S2) and all pairs should be in the set or w1==w2.

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        if len(words1)!=len(words2):
            return False

        pairs = set(map(tuple, pairs))
        
        return all([w1==w2 or (w1, w2) in pairs or (w2, w1) in pairs for (w1, w2) in zip(words1, words2)])