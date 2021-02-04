# Run days one by one until the pattern repeats. Once the pattern repeats, find a cycle and do N=N%cycle. We the process remaining N one by one.

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        d = {}
        is_forwarded = False

        while N > 0:
            
            if not is_forwarded:
                state_key = tuple(cells)
                if state_key in d:
                    cycle_len = d[state_key] - N
                    N = N % cycle_len
                    is_forwarded = True
                else:
                    d[state_key] = N

            if N > 0:
                N -= 1
                cells = self.nextDay(cells)

        return cells


    def nextDay(self, cells):
        ret = [0] * len(cells)
        for i in range(1, len(cells)-1):
            ret[i] = int(cells[i-1] == cells[i+1])
        return ret