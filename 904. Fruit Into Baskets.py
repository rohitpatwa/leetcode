# 3 variables to store info of last_fr, 2nd_last_fr and last_fr_count. If x==last_fr, local_max+=1, if x==2nd_last, swap the two and last_fr_count=1.

class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        # For keeping track of identity of last fruits
        last_f, second_last_f = -1, -1
        
        # Count of most recent fruit in series
        last_fruit_count = 0
        global_max, local_max = 0, 0
        
        
        for x in tree:
            
            # x is same as the last fruit seen
            # increment the last fruit count and move ahead
            if x==last_f:
                last_fruit_count += 1
                local_max += 1
            
            # x is same as the second last fruit seen
            # Second last becomes the last and vice versa
            # and last fruit count becomes 1
            elif x==second_last_f:
                second_last_f, last_f = last_f, second_last_f
                last_fruit_count = 1
                local_max += 1
            
            # when a new fruit is encountered
            # last becomes second last and new one becomes last
            # last fruit count becomes 1
            else:
                second_last_f, last_f = last_f, x
                local_max = last_fruit_count + 1
                last_fruit_count = 1
            
            # Update ulobal max after ever iteration
            global_max = max(global_max, local_max)
            
        return global_max