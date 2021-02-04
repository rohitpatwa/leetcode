# Iterate over logs and separate letter logs and digit logs. Sort letter logs and append them together in the result.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for l in logs:
            if l.split()[1] != l.split()[1].upper():
                letter_logs.append(l)
            else:
                digit_logs.append(l)
        
        letter_logs = sorted([(x.split()[1:], x.split()[0]) for x in letter_logs])
        
        return [x[1] + " " + " ".join(x[0]) for x in letter_logs] + digit_logs