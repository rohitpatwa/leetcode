# Iterate over the enitre array. Insert counts only if != 1. Pop repeated occurances of characters.

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        run = 1
        prev = chars[0]
        i = 1
        
        while i<len(chars):
            c = chars[i]
            if c==prev:
                run += 1
                chars.pop(i)  # this makes up for incrementing i
            else:
                if run>1:  # insert run only if > 1
                    for r in str(run):
                        chars.insert(i, r)  # Insert run digit at i and increment i
                        i += 1
                prev = c  # now lookout for the new char
                run = 1  # which has run of 1
                i += 1  # increment i for jumping to the next itereation
                
        if run>1:  # Add the last run to the result
            for r in str(run):
                chars.append(r)
            
        return len(chars)
            