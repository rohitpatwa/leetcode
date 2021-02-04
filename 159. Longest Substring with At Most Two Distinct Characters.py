# Store the value and counts of last char and second last char. Then there will be 3 cases for every new char.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s)<=2:
            return len(s)
        last_c, second_last_c = s[0], None
        last_count, second_last_count = 1, 0
        res = 1
        
        curr_max = 1
        for c in s[1:]:
            if c==last_c:
                last_count += 1
                curr_max += 1
            
            elif c==second_last_c:
                last_c, second_last_c = second_last_c, last_c
                curr_max += 1
                last_count = 1
            else:
                second_last_c, last_c = last_c, c 
                curr_max = last_count + 1
                last_count = 1
                
            res = max(res, curr_max)
        return res
                
                
                
        
        