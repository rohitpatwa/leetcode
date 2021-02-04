# Create two dict of identical and rotation numbers which satisfy the condition. Compare every num[i] with num[~i] as per id and rot dicts.

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        
        rev = num[::-1]
        identical = set(["0", "8", "1"])
        rotation = {"6":"9", "9":"6"}

        for i in range(len(num)//2+1):
            if num[i] in identical and num[i] == rev[i]:
                continue
            elif num[i] in rotation and rotation[num[i]] == rev[i]:
                continue
            return False
        return True