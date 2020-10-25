# Store sign of x. Convert x in str, reverse str, convert str back to int, multiply it with it's sign. Remember to take mods at the end.

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        
        x1 = str(x)
        x1 = x1[::-1]
        x2 = int(x1)
        x2 *= sign
        return x2 if -2147483648 < x2 < 2147483647 else 0