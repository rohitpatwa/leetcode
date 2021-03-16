# Iterate through the string till you find the outermost closing bracket. Send the internal substring for a recursive call. Multiply with number outside.

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        i = 0

        while i < len(s):
            if s[i].isalpha():
                res += s[i]
                i += 1
            else:
                num = ""
                while s[i] != "[":
                    num += s[i]
                    i += 1
                num = int(num)
                
                i += 1
                sub = ""
                bracket_count = 1
                while bracket_count != 0:
                    if s[i] == '[':
                        bracket_count += 1
                    elif s[i] == ']':
                        bracket_count -= 1
                    sub += s[i]
                    i += 1
                
                res += num * self.decodeString(sub[:-1])
        return res
