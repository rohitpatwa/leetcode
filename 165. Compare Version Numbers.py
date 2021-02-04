# Split on . and compare on each part. Iterate on max(len(v1), len(v2)). If index out of bounds, use 0 as filler.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        for i in range(max(len(version1), len(version2))):
            
            v1 = int(version1[i]) if i<len(version1) else 0
            v2 = int(version2[i]) if i<len(version2) else 0

            if v1>v2:
                return 1
            elif v2>v1:
                return -1

        return 0
