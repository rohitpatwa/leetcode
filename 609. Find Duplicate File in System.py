# Split paths and files. The split files. The split filename and content. Add content to dict and full path as value in a list. 

import re

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = {}
        for p in paths:
            path, files = p.split(' ', 1)
            files = files.split(r')')
            for f in files:
                if not f:
                    continue
                f_name, content = f.split('(')
                d[content] = d.get(content, []) + [f'{path}/{f_name.strip()}']
            
            
        res = []
        for x in d.values():
            if len(x)>1:
                res.append(x)
        return res