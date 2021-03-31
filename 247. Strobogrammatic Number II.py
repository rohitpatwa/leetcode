# Add left and right numbers together. For the center digit, add identical number only(0,1,8).

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        self.identitical = ["0","1","8"]
        self.compliment = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        self.helper([None]*n, 0, n-1, res)
        return res

    def helper(self, curr, l, r, res):
        if l>r:
            num = ''.join(curr[:])
            if num == str(int(num)):
                res.append(num)
        
        elif l==r:
            for c in self.identitical:
                curr[l] = c
                self.helper(curr, l+1, r-1, res)

        else:
            for c in self.compliment.keys():
                curr[l] = c
                curr[r] = self.compliment[c]
                self.helper(curr, l+1, r-1, res)