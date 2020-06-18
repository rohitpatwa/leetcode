# Split the emails at @. Apply rules through regex and add the resultant email in a set.

import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        res = set()
        for e in emails:
            local, domain = e.split('@')
            local = re.sub(r'\+.*', '', local)
            local = local.replace('.', '')
            res.add(local + '@' + domain)
        return len(res)
