# Iterate over the enitre array. Insert counts only if != 1. Pop repeated occurances of characters.

class Solution:
    def compress(self, chars: List[str]) -> int:
        i, prev, count = 0, None, 0

        while i<len(chars):
            
            if not prev:
                count = 1
                prev = chars[0]
                i += 1
            
            elif chars[i] == prev:
                count += 1
                chars.pop(i) # this makes up for incrementing i
                
            else:
                prev = chars[i] # update prev
                if count!=1: # insert count only if != 1
                    for k in list(str(count)):
                        chars.insert(i, k)
                        i += 1 # insert every digit at next index
                i += 1 # bring the pointer to next char
                count = 1 # because we've already seen the next char
        
        # insert the last count if !=1
        if count!=1:
            chars += list(str(count))
        return len(chars)
            