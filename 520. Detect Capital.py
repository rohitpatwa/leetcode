# Check if word is all upper or all lower. elif check if word is one capital and all lower. Else return False.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word==word.upper() or word==word.lower():
            return True
        if word[0] == word[0].upper() and word[1:]==word[1:].lower():
            return True
        return False