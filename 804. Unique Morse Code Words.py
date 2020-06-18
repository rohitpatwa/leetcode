# Create a set and add all the codes in it. Return length.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        res = set()
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
        for w in words:
            code = ""
            for c in w:
                code += codes[ord(c) - 97]
            res.add(code)
        return len(res)
                