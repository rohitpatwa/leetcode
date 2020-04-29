# Find min lenghth string, iterate over it and keep checking if the letter is same across all other strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs)==0:
            return ''
        elif len(strs)==1:
            return strs[0]
        min_len = min([len(x) for x in strs])
        
        
        res = 0
        for i in range(min_len):
            flag = True
            c = strs[0][i]
            for s in strs:
                if s[i]!=c:
                    flag=False
                    break

            if not flag:
                break
            else:
                res += 1
        return strs[0][:res]