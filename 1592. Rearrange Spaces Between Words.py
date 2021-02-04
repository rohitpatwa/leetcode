# Count the number of words and spaces separately. Distribute the spaces between the words.

class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        spaces = text.count(" ")
        text = text.split()
        num_words = len(text)
        
        if num_words==1:
            return text[0] + " "*spaces
        
        num_spaces = spaces//(num_words-1)
        leftover = spaces % (num_words-1)
        text = (num_spaces * " ").join(text) + " "*leftover
        return text